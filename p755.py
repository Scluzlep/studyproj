from math import factorial
stop_num = float(input("Enter a number: "))
i = 0
e = 0
while 1 / factorial(i) > stop_num:
    q = 1 / factorial(i)
    e = e + q
    i = i + 1
print(e)
