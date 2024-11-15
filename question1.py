x = eval(input("Enter a number: "))
z = eval(input("Enter another number: "))
if z > 0:
    if x >= 5:
        y = x ** 0.5 + z
    elif 0 < x < 5:
        y = x ** 3 + z
    elif x == 0:
        y = 0 + z
    else:
        y = (-2 / x) + z
elif z < 0:
    if x >= 5:
        y = x ** 0.5 - z
    elif 0 < x < 5:
        y = x ** 3 - z
    elif x == 0:
        y = 0 - z
    else:
        y = (-2 / x) - z
print(y)
