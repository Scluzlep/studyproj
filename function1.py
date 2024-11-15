import math

x = eval(input("Enter a number: "))
if x > 10:
    y = 1/x
elif x > 1:
    y = math.sqrt(x)
elif x > 0:
    y = math.exp(x)
else:
    y = abs(x)
print(y)
