def country(filename):
    global capital
    capital = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for x in f:
            line = x.strip().split(',')
            capital[line[0]] = line[1]
    return capital


def query():
    while True:
        countries = input('请输入一个国家：')
        if countries == '退出':
            break
        else:
            print('这个国家的首都是：', capital.get(countries, '没有这个国家'))


if __name__ == '__main__':
    capital = country('country.csv')
    query()
