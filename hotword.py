with open('egstory.txt','r',encoding='utf-8-sig') as f:
    s1 = f.read()
    s2 = ''
    s3 = []
    s1 = s1.lower()
    s1 = s1.replace('\n',' ')
    for i in s1:
        if i.isalnum() or i == ' ':
            s2 += i
        else:
            s2 += ' '
    L = s2.split(' ')
    for k in L:
        if L.count(k) > 5 and k not in s3:
            s3.append(k)
print(s3)

