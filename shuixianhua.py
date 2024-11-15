# num = eval(input('输入一个三位数：'))
s = 0
for num in range(100, 1000):
    hundred_digit = num // 100
    ten_digit = num // 10 % 10
    one_digit = num % 10
    num2 = hundred_digit ** 3 + ten_digit ** 3 + one_digit ** 3
    if num == num2:
        s = s + 1
        print(f'{num}是水仙花数', end=' ')
        num = num + 1
    # else:
    #     print(f'{num}不是水仙花数')
print()
print('有', s, '个水仙花数', sep='')
