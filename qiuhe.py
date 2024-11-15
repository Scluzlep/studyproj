x = eval(input('input a num'))
i = 1
s = 0
p = 1
if 0 < x < 1:
    while p > 1e-5:
        numerator = x ** i
        denominator = 2 * i - 1
        p = numerator / denominator
        s = s + p
        i = i + 1
    print(s)
else:
    print('Invalid x')
