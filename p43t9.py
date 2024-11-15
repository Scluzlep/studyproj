import math

a=eval(input('输入a:'))
b=eval(input('输入b:'))
x = (-b + math.sqrt(2 * a * math.sin(math.radians(60)) * math.cos(math.radians(60))))/(2*a)
print(x)
