birthday = input('输入出生年月（如20010212）')
year = int(birthday[0:4])
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('你是闰年出生')
else:
    print('你不是闰年出生')
