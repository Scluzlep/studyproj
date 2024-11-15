s = 0
flag = 1
n = int(input("Enter a number: "))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if n > 0:
    for i in range(1, n + 1):
        if i == 1:
            numerator = 1
        else:
            numerator = i - 1
        denominator = fibonacci(i + 1)
        q = numerator / denominator
        s = s + flag * q
        flag = - flag
    print('{:.6f}'.format(s))
else:
    print("Invalid input")