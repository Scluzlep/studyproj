s = [['张三', 93], ['李四', 58], ['王五', 74]]
s2 = []
for i in s:
    if i[1] >= 90:
        i.append('良好')
        s2.append(i)
    elif i[1] >= 60:
        i.append('及格')
        s2.append(i)
    else:
        i.append('不及格')
        s2.append(i)
print(s2)
