num = int(input("输入一个四位整数："))
thousands_num = num // 1000
hundreds_num = num // 100 % 10
tens_num = num // 10 % 10
ones_num = num % 10
dnum = thousands_num + hundreds_num * 10 + tens_num * 100 + ones_num * 1000
mima = dnum + thousands_num + hundreds_num + tens_num + ones_num
print(mima)
