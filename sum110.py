def sum110(n):
    if n == 1:
        return 1
    else:
        return n + sum110(n - 1)

print(sum110(10))