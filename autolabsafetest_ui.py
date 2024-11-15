import base64
import sys
import json
from difflib import SequenceMatcher
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox, \
    QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup

# 读取 questions.json 文件
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as f:
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


# 自动答题逻辑
def start_auto_answer(driver, username, password, captcha, mode, confirm_callback):
    # 加载题目数据
    questions_data = load_questions()

    # 输入账号和密码
    username_input = driver.find_element(By.ID, "txtUserAccount")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "txtPassword")
    password_input.send_keys(password)

    # 输入验证码
    captcha_input = driver.find_element(By.ID, "txtIdentifyingCode")
    captcha_input.send_keys(captcha)

    # 点击登录按钮
    login_button = driver.find_element(By.ID, "btnLogin")
    login_button.click()
    time.sleep(3)

    # 查找“进入系统”按钮并点击
    enter_system_button = driver.find_element(By.XPATH, "//a[contains(text(), '进入系统')]")
    enter_system_button.click()
    time.sleep(3)

    # 跳转到考试或练习页面
    if mode == "考试":
        driver.get("http://syspxxt.ahstu.edu.cn/aqks/Student/TestList.aspx")
    else:
        driver.get("http://syspxxt.ahstu.edu.cn/aqks/Student/PracticeList.aspx")

    time.sleep(2)

    # 用户确认已进入考试/练习页面
    confirm_continue = QMessageBox.question(
        confirm_callback,
        "确认进入页面",
        "请确认已进入考试/练习页面",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.Yes
    )

    if confirm_continue == QMessageBox.Yes:
        # 等待页面加载 iframe
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='layui-layer-iframe']"))
        )

        # 获取 iframe 的 src 属性并打开实际的考试/练习页面
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe[id^='layui-layer-iframe']")
        iframe_src = iframe.get_attribute("src")
        driver.get(iframe_src)

        # 获取页面源代码并解析HTML
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 创建 ABCD 到 1234 的映射
        option_map = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6'}
        tf_map = {'正确': 'T', '错误': 'F'}

        # 自动答题实现
        question_rows = soup.find_all('tr', id=True)
        for i, question_row in enumerate(question_rows, start=1):
            # 提取题目 ID 和题干
            question_id = question_row['id'].replace("tr", "")
            question_text_element = question_row.find('h4')
            question_text = question_text_element.text.strip() if question_text_element else ""

            # 查找选项
            options_elements = question_row.find_all('label')
            options_text = [opt.text.strip() for opt in options_elements]

            # 模糊匹配最优题目
            best_match = find_best_match(question_text, questions_data)
            if not best_match:
                continue

            correct_answer = best_match['correct_answer'].strip()

            # 根据题型自动作答
            if i <= 20:  # 单选题
                converted_choice = option_map.get(correct_answer, None)
                if converted_choice:
                    radio_button = driver.find_element(By.ID, f"rdb{question_id}{converted_choice}")
                    radio_button.click()

            elif 21 <= i <= 30:  # 多选题
                correct_answers = best_match['correct_answer'].split(',')
                for answer in correct_answers:
                    converted_choice = option_map.get(answer.strip(), None)
                    if converted_choice:
                        checkbox = driver.find_element(By.ID, f"cbl{question_id}{converted_choice}")
                        checkbox.click()

            elif 31 <= i <= 50:  # 判断题
                converted_choice = tf_map.get(correct_answer, None)
                if converted_choice:
                    radio_button = driver.find_element(By.ID, f"rdb{question_id}{converted_choice}")
                    radio_button.click()

        # 用户确认退出
        confirm_close = QMessageBox.question(
            confirm_callback,
            "确认退出",
            "按 Enter 键退出并关闭浏览器（请手动交卷后）",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )

        if confirm_close == QMessageBox.Ok:
            driver.quit()

# PyQt5 界面
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自动答题系统")
        self.setGeometry(100, 100, 400, 300)

        self.driver = None  # 浏览器驱动

        # 创建控件
        self.label_user = QLabel("账号:")
        self.input_user = QLineEdit()

        self.label_pass = QLabel("密码:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)

        self.label_captcha = QLabel("验证码:")
        self.input_captcha = QLineEdit()

        self.captcha_image_label = QLabel("加载验证码...")
        self.captcha_image_label.setAlignment(Qt.AlignCenter)

        self.label_mode = QLabel("选择模式:")
        self.combo_mode = QComboBox()
        self.combo_mode.addItems(["考试", "练习"])

        self.button_login = QPushButton("登录")
        self.button_login.clicked.connect(self.handle_login)

        self.button_confirm_continue = QPushButton("确认进入页面并继续")
        self.button_confirm_continue.clicked.connect(self.confirm_continue)
        self.button_confirm_continue.setVisible(False)

        self.button_confirm_close = QPushButton("确认退出并关闭浏览器（请手动交卷后）")
        self.button_confirm_close.clicked.connect(self.confirm_close)
        self.button_confirm_close.setVisible(False)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.input_pass)

        captcha_layout = QHBoxLayout()
        captcha_layout.addWidget(self.captcha_image_label)
        captcha_layout.addWidget(self.input_captcha)

        layout.addLayout(captcha_layout)
        layout.addWidget(self.label_mode)
        layout.addWidget(self.combo_mode)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_confirm_continue)
        layout.addWidget(self.button_confirm_close)

        self.setLayout(layout)

        self.start_browser()

    def start_browser(self):
        # 加载 Edge 浏览器
        options = Options()
        options.add_argument("--disable-features=AutomaticHttps")
        options.add_argument(r"user-data-dir=C:\edgeprofile")

        self.driver = webdriver.Edge(options=options)
        self.driver.get("http://syspxxt.ahstu.edu.cn/aqks/Index.aspx")
        time.sleep(2)

        # 获取验证码图片并显示
        captcha_element = self.driver.find_element(By.ID, "imgIdentifyingCode")
        captcha_base64 = captcha_element.screenshot_as_base64  # 获取Base64编码的图片

        # 解码Base64为图片数据
        img_data = base64.b64decode(captcha_base64)

        # 使用 QImage 显示验证码图片
        qimage = QImage.fromData(img_data)
        pixmap = QPixmap.fromImage(qimage)
        self.captcha_image_label.setPixmap(pixmap)

    def handle_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()
        captcha = self.input_captcha.text()
        mode = self.combo_mode.currentText()

        if not username or not password or not captcha:
            QMessageBox.warning(self, "警告", "请填写所有字段")
            return

        # 替换原有提示为信息框
        QMessageBox.information(self, "登录成功", f"您选择了 {mode}, 请确认页面加载后继续...")

        # 显示确认继续按钮
        self.button_confirm_continue.setVisible(True)

    def confirm_continue(self):
        # 执行进入考试/练习的操作
        QMessageBox.information(self, "继续", "请确认已进入考试/练习页面，操作将继续...")

        # 开始自动答题
        start_auto_answer(self.driver, self.input_user.text(), self.input_pass.text(), self.input_captcha.text(), self.combo_mode.currentText())

        # 显示确认关闭按钮
        self.button_confirm_continue.setVisible(False)
        self.button_confirm_close.setVisible(True)

    def confirm_close(self):
        # 提示手动交卷
        QMessageBox.information(self, "关闭浏览器", "请确认已经手动交卷后再退出系统。")

        # 关闭浏览器
        self.driver.quit()

        # 退出程序
        self.close()

# 主程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

