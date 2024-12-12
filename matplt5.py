import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# import xlrd

plt.rcParams['font.sans-serif'] = 'SimHei'
data = pd.read_excel('学生成绩表.xls')
print(data)
name = data['姓名']
score1 = data['Python程序设计']
score2 = data['数据库']
score3 = data['数据结构']
score4 = data['数据处理']
plt.plot(name, score1, color='red', marker='o', linestyle='-', label='Python程序设计')
plt.plot(name, score2, color='blue', marker=',', linestyle='-', label='数据库')
plt.plot(name, score3, color='green', marker='<', linestyle='-', label='数据结构')
plt.plot(name, score4, color='black', marker='.', linestyle='-', label='数据处理')
plt.legend(loc='upper left')
plt.title('学生成绩')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.show()
