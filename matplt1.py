import matplotlib.pyplot as plt

font_path = 'simhei.ttf'
plt.rcParams['font.sans-serif'] = 'SimHei'
x = ['张三', '李四', '王五', '刘一']
y1 = [67, 65, 93, 73]
y2 = [56, 78, 79, 56]
plt.plot(x, y1, color='red', marker='o', linestyle=':', label='Python程序设计')
plt.plot(x, y2, color='blue', marker='x', linestyle='-', label='数据库')
plt.legend(loc='upper left')
plt.title('学生成绩')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.show()
