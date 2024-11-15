n = int(input("Enter a number: "))
s = 0
flag = -1
for i in range(1,n+1):
    s = s + (flag)*(1/i)
    flag = -flag
print(s)