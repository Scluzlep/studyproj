def t1(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result


def t2(num):
    result = 1
    for i in (2, 9):
        result = result + ((num ** i) / i)
    return result


def t3(num):
    s = []
    for i in range(1, num + 1):
        if num % i == 0:
            s.append(i)


if __name__ == '__main__':
    x = eval(input('请输入一个数：'))
    n = int(input('请输入序号：'))
    if n == 1:
        print(t1(x))
    elif n == 2:
        print(t2(x))
    elif n == 3:
        print(t3(x))
    else:
        print('输入错误')
