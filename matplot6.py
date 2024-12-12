import pandas as pd
import matplotlib.pyplot as plt

# import numpy as np
# import xlrd

plt.rcParams['font.sans-serif'] = 'SimHei'

class1_score = pd.read_excel('学生成绩表.xls')
class2_score = pd.read_excel('211班成绩表.xls')
class1 = [class1_score['Python程序设计'].mean(), class1_score['数据库'].mean(), class1_score['数据结构'].mean(),
          class1_score['数据处理'].mean(),]
class2 = [class2_score['Python程序设计'].mean(), class2_score['数据库'].mean(), class2_score['数据结构'].mean(),
          class2_score['数据处理'].mean(),]

width = 0.35
x_index = range(len(class1))
plt.bar([i - width / 2 for i in x_index], class1, color='red', label='一班', alpha=0.6, width=width)
plt.bar([i + width / 2 for i in x_index], class2, color='blue', label='二班', alpha=0.6, width=width)
plt.legend(loc='upper left')
plt.title('两个班的平均成绩对比图')
plt.xlabel('科目')
plt.ylabel('成绩')
plt.xticks(x_index, ['Python程序设计', '数据库', '数据结构', '数据处理'])
plt.show()
