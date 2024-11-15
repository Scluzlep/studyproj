from bs4 import BeautifulSoup
import json

with open('练习试卷详情2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')
questions_list = []

for section in soup.find_all('h3'):
    section_title = section.get_text(strip=True)

    # 查找每个题目
    for question_block in section.find_next_siblings('table')[0].find_all('tr', id=True):
        # 提取题号和题目
        question_text = question_block.find('h4').get_text(strip=True)

        # 提取题目ID
        question_id = question_block['id']  # 提取id属性

        # 检查部分标题是否包含“判断题”，并设置固定选项
        if "判断题" in section_title:
            options = ["正确", "错误"]  # 固定选项
        else:
            # 提取其他选项，排除“正确答案”和“我的答案”，并去掉换行符
            options = [
                option.get_text(strip=True).replace('\n', '') for option in question_block.find_all('p')[1:-2]
            ]

        # 提取我的答案
        my_answer_tag = question_block.find('p', string=lambda x: x and '我的答案' in x)
        my_answer = my_answer_tag.get_text(strip=True).replace("我的答案:", "").strip() if my_answer_tag else ""

        # 提取正确答案
        correct_answer_tag = question_block.find('p', string=lambda x: x and '正确答案' in x)
        correct_answer = correct_answer_tag.get_text(strip=True).replace("正确答案:", "") if correct_answer_tag else ""

        # 构建题目数据
        question_data = {
            'section': section_title,  # 加入部分标题
            'question': question_text,
            'question_id': question_id,  # 加入题目ID
            'options': options,
            'correct_answer': correct_answer.strip()
        }
        questions_list.append(question_data)

# 将提取到的题目数据转换为JSON
with open('questions.json', 'w', encoding='utf-8') as json_file:
    json.dump(questions_list, json_file, ensure_ascii=False, indent=4)

print("题库已成功转换为JSON格式！")
