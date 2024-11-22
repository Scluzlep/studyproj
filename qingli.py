s = 'Boys are.brave, and the girls are brave as the boys'
s = s.lower()
s2 = ''
for i in s:
    if i.isalnum():
        s2 += i
    elif i == ' ':
        s2 += i
    else:
        s2 += ' '
L = s2.split()
print(L)
s5 = []
for i in L:
    if L.count(i) >= 2 and i not in s5:
        s5.append(i)
print(s5)
