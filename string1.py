type = 0
digit = 0
else_str = 0
a_str = input('输入一个字符串')
for i in a_str:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        type += 1
    else:
        else_str += 1
print(f'type={type}, digit={digit}, else_str={else_str}')
