n = int(input("输入一个正整数:"))
s = 0
for i in range(1,n):
    if n % i == 0:
        s = s + i
if s == n:
    print(n,'是完美数')
else:
    print(n,'不是完美数')

