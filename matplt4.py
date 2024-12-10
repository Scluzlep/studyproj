import matplotlib.pyplot as plt

font_path = 'simhei.ttf'
plt.rcParams['font.sans-serif'] = 'SimHei'
x = ['张三', '李四', '王五', '刘一']
y1 = [67, 65, 93, 73]
y2 = [56, 78, 79, 56]
plt.bar(x, y1, color='red', label='Python程序设计', alpha=0.5)
plt.bar(x, y2, color='blue', label='数据库', alpha=0.5)
plt.legend(loc='upper left')
plt.title('学生成绩')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.show()
