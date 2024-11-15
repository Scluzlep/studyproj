a, b, c = eval(input('输入一元二次方程的三个系数,用逗号隔开(ax^2+bx+c=0):'))
delta = b ** 2 - 4 * a * c
if a == 0:
    x = -c / b
    print('是一元一次方程,x=', x, sep='')
else:
    if delta < 0:
        print('无实数根,delta=', delta, sep='')
    elif delta == 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        print('一个实数根,', 'x1=', x1, sep='')
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print('两个实数根', 'x1=', x1, ',x2=', x2, sep='')
