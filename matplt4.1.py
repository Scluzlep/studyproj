import matplotlib.pyplot as plt

font_path = 'simhei.ttf'
plt.rcParams['font.sans-serif'] = 'SimHei'
x = ['张三', '李四', '王五', '刘一']
y1 = [67, 65, 93, 73]
y2 = [56, 78, 79, 56]
x1 = [1,3,5,7]
x2 = [2,4,6,8]

plt.bar(x1, y1, color='red', label='Python程序设计', alpha=1,)
plt.bar(x2, y2, color='blue', label='数据库', alpha=1,)
plt.legend(loc='upper left')
plt.title('学生成绩')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.xticks(x1, x)
plt.show()
