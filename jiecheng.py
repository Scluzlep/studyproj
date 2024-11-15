s = 0
flag = -1
n = 1
while n <= 10:
    t = 1
    i = 1
    while i <= n:
        t = t * i
        i = i + 1
    s = s + t * flag
    flag = -flag
    n = n + 1
print(s)
