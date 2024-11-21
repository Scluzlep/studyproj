s1 = '50 56 80 74 40'
s2 = s1.split(' ')
s3 = []
for i in s2:
    if int(i) < 60:
        s3.append(i)
print(s3)
