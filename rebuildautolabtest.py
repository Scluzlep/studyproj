from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import json
from selenium.webdriver.edge.options import Options
from difflib import SequenceMatcher
import os
import shutil

# 创建 ABCD 到 1234 的映射
OPTION_MAP = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6'}

# 创建 正确/错误 到 T/F 的映射
TF_MAP = {'正确': 'T', '错误': 'F'}


# 读取 questions.json 文件
def load_questions():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    questions_file = os.path.join(base_dir, "questions.json")
    with open(questions_file, 'r', encoding='utf-8') as f:
        return json.load(f)


# 通过题目内容进行模糊匹配
def find_best_match(question_text, questions_data):
    best_match = None
    highest_ratio = 0.0
    for question in questions_data:
        question_content = question['question']
        match_ratio = SequenceMatcher(None, question_text, question_content).ratio()
        if match_ratio > highest_ratio:
            highest_ratio = match_ratio
            best_match = question
    return best_match if highest_ratio > 0.8 else None  # 设定匹配的最低阈值为 0.8


def edge_init():
    global driver
    # 创建 Edge 选项
    options = Options()
    # 禁用自动 HTTPS
    base_dir = os.path.dirname(os.path.abspath(__file__))
    user_data_dir = os.path.join(base_dir, "edgeprofile")
    options.add_argument("--disable-features=AutomaticHttps")
    options.add_argument(f'user-data-dir={user_data_dir}')
    # 启动Edge浏览器
    driver = webdriver.Edge(options=options)


def openweb_sleep(link, sleeptime):
    # 打开网站
    driver.get(link)
    # 等待页面加载
    time.sleep(sleeptime)


def login():
    # 输入账号和密码（账号和密码相同）
    username_input = driver.find_element(By.ID, "txtUserAccount")
    username_input.send_keys(str(input('输入你的账号:')))
    password_input = driver.find_element(By.ID, "txtPassword")
    password_input.send_keys(str(input('输入你的密码:')))
    # 手动输入验证码
    captcha_input = driver.find_element(By.ID, "txtIdentifyingCode")
    captcha_img = driver.find_element(By.ID, "imgIdentifyingCode").get_attribute("src")
    print(f"请手动输入验证码: {captcha_img}")
    captcha_code = input("请输入验证码: ")
    captcha_input.send_keys(captcha_code)
    # 点击登录按钮
    login_button = driver.find_element(By.ID, "btnLogin")
    login_button.click()
    # 等待登录完成
    time.sleep(3)
    # 查找“进入系统”按钮并点击
    enter_system_button = driver.find_element(By.XPATH, "//a[contains(text(), '进入系统')]")
    enter_system_button.click()
    # 等待页面加载
    time.sleep(3)


def enter_test_exercise(choice):
    if choice == "1":
        openweb_sleep("http://syspxxt.ahstu.edu.cn/aqks/Student/TestList.aspx", 0)
        print("跳转到考试页面")
    elif choice == "2":
        openweb_sleep("http://syspxxt.ahstu.edu.cn/aqks/Student/PracticeList.aspx", 0)
        print("跳转到练习页面")
    else:
        print("无效输入，请输入 1 或 2")
        driver.quit()
    # 等待页面加载
    time.sleep(2)
    # 用户确认已进入考试/练习页面
    input("请确认已进入考试/练习页面后按 Enter 键继续...")


def analyse_htm():
    global soup
    # 等待页面加载 iframe
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='layui-layer-iframe']"))
    )
    # 提取 iframe 的 src 属性
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[id^='layui-layer-iframe']")
    iframe_src = iframe.get_attribute("src")
    print(f"考试/练习页面的链接: {iframe_src}")
    # 打开实际的考试/练习页面
    driver.get(iframe_src)
    # 获取页面源代码
    html = driver.page_source
    # 解析HTML
    soup = BeautifulSoup(html, 'html.parser')


# 清理选项
def clean_options(options_text):
    cleaned_options = []
    for option in options_text:
        # 去掉前后空白字符
        cleaned_option = option.strip()
        # 替换特殊字符
        cleaned_option = cleaned_option.replace('\xa0', '').replace('\n', '')
        if "正确" in cleaned_option or "错误" in cleaned_option:
            cleaned_options = ['正确', '错误']
            break  # 找到判断题后退出循环
        # 如果选项不为空且去掉特殊字符后仍然有内容，则加入 cleaned_options
        if cleaned_option:
            # 可以根据需求进一步分割选项（如果选项包含多个值）
            cleaned_options.extend(cleaned_option.split())
    # 如果 cleaned_options 不等于 判断题的选项，则删除最后一项
    if cleaned_options != ['正确', '错误'] and cleaned_options:
        cleaned_options.pop()  # 删除最后一项（如 'ABCD'）
    # 将选项连接为一个字符串，使用空格分隔
    result = ' '.join(cleaned_options)
    return result


# 执行结束后删除配置文件
def auto_rmprofile():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    user_data_dir = os.path.join(base_dir, "edgeprofile")
    questions_file = os.path.join(base_dir, "questions.json")

    try:
        # 删除用户数据目录
        if os.path.exists(user_data_dir):
            shutil.rmtree(user_data_dir)  # 删除整个目录及其内容
            print(f"已删除配置目录: {user_data_dir}")

        # 删除 questions.json 文件
        if os.path.exists(questions_file):
            os.remove(questions_file)
            print(f"已删除题库文件: {questions_file}")
    except Exception as e:
        print(f"删除文件时发生错误: {e}")


# 自动答题实现
def auto_answer():
    # 查找每一道题目及其选项
    question_rows = soup.find_all('tr', id=True)

    for i, question_row in enumerate(question_rows, start=1):
        # 提取题目 ID
        question_id = question_row['id'].replace("tr", "")

        # 查找题干
        question_text_element = question_row.find('h4')
        question_text = question_text_element.text.strip() if question_text_element else ""

        # 查找选项
        options_elements = question_row.find_all('p')
        options_text = [opt.text.strip() for opt in options_elements]

        result = clean_options(options_text)

        print(f"题号 {i}: {question_text}")
        print(f"选项: {result}")

        # 模糊匹配最优题目
        best_match = find_best_match(question_text, questions_data)

        if not best_match:
            print(f"未找到匹配的题目，跳过...")
            continue

        print(f"匹配到的正确答案: {best_match['correct_answer']}")

        # 根据题型自动作答
        if i <= 20:  # 单选题
            correct_answer = best_match['correct_answer'].strip()
            converted_choice = OPTION_MAP.get(correct_answer, None)
            if converted_choice:
                radio_button = driver.find_element(By.ID, f"rdb{question_id}{converted_choice}")
                radio_button.click()
            else:
                print(f"未找到单选答案的映射: {correct_answer}")

        elif 21 <= i <= 30:  # 多选题
            correct_answers = best_match['correct_answer'].split(',')
            for answer in correct_answers:
                answer = answer.strip()
                converted_choice = OPTION_MAP.get(answer, None)
                if converted_choice:
                    checkbox = driver.find_element(By.ID, f"cbl{question_id}{converted_choice}")
                    checkbox.click()
                else:
                    print(f"未找到多选答案的映射: {answer}")

        elif 31 <= i <= 50:  # 判断题
            correct_answer = best_match['correct_answer'].strip()
            converted_choice = TF_MAP.get(correct_answer, None)
            if converted_choice:
                radio_button = driver.find_element(By.ID, f"rdb{question_id}{converted_choice}")
                radio_button.click()
            else:
                print(f"未找到判断题答案的映射: {correct_answer}")


if __name__ == '__main__':
    try:
        # 加载题目数据
        questions_data = load_questions()
        # 启动edge
        edge_init()
        # 打开网页
        openweb_sleep("http://syspxxt.ahstu.edu.cn/aqks/Index.aspx", 2)
        # 登录
        login()
        # 进入考试/练习
        enter_test_exercise(choice=input("请输入 1 选择考试，输入 2 选择练习："))
        # 解析网页
        analyse_htm()
        # 开始自动答题
        auto_answer()
        # 保持浏览器打开，等待用户输入
        input("手动交卷后按 Enter 键退出并关闭浏览器...")
    finally:
        # 无论程序是否正常退出，都会调用清理函数
        driver.quit()  # 关闭浏览器
        auto_rmprofile()  # 删除配置文件和题库文件
