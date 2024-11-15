from math import sqrt

a = eval(input('输入a:'))
b = eval(input('输入b:'))
c = eval(input('输入c:'))
if 0 < c < a + b and 0 < b < a + c and 0 < a < b + c:
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print('三角形面积为', s)
else:
    print('不是三角形')
