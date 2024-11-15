str1 = input("输入子字符串")
str2 = input('输入母字符串')
num = 0
for i in str1:
    if str2.find(i) != -1:
        num += 1
rate = num / len(str2)
print('重复率{:.1%}'.format(rate))
