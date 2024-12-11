import matplotlib.pyplot as plt


def plt_bar(x, y1, y2):
    width = 0.35
    x_index = range(len(x))

    plt.bar([i - width / 2 for i in x_index], y1, color='red', label='Python程序设计', alpha=0.6, width=width)
    plt.bar([i + width / 2 for i in x_index], y2, color='blue', label='数据库', alpha=0.6, width=width)
    left_bar = zip((i - width / 2 for i in x_index), y1)
    right_bar = zip((i + width / 2 for i in x_index), y2)
    plt.legend(loc='upper left')
    plt.title('学生成绩')
    plt.xlabel('姓名')
    plt.ylabel('成绩')
    plt.xticks(x_index, x)
    for i, j in left_bar:
        plt.text(i, j + 0.5, str(j), ha='center', va='bottom')
    for i, j in right_bar:
        plt.text(i, j + 0.5, str(j), ha='center', va='bottom')
    plt.show()


def init_d():
    plt.rcParams['font.sans-serif'] = 'SimHei'


if __name__ == '__main__':
    name = ['张三', '李四', '王五', '刘一']
    score1 = [67, 65, 93, 73]
    score2 = [56, 78, 79, 56]
    init_d()
    plt_bar(name, score1, score2)
