s = 0
for num in range(1000,10000):
    strnum = str(num)
    dnum = strnum[::-1]
    if dnum == strnum:
        s = s + num
print(s)