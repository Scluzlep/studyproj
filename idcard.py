id_num = input("Enter your ID Number: ")
if int(id_num[16]) % 2 == 0:
    sex = '女'
else:
    sex = '男'
birthday = id_num[6:14]
age = 2024 - int(birthday[:4])
print(f'你是{sex}性，生日是{birthday}，年龄{age}岁。')
