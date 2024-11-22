with open('name.txt','r',encoding='utf-8') as f:
    s1 = f.read()
    f.seek(0)
    s2 = f.readlines()
print(s1)
print(s2)
