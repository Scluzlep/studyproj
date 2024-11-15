from math import sqrt

num = 0
for i in range(1, 101):
    if i == 1:
        print(f'{i}不是素数')
    elif  1 < i < 4:
        print(f'{i}是素数')
    else:
        for n in range(2, int(sqrt(i)) + 1):
            if i % n == 0:
                print(f'{i}不是素数')
                break
        else:
            print(f'{i}是素数')
