last_3_num = 106
sum1 = 0
for i in range(1,last_3_num+1):
    if i % 2 == 0 or i % 3 == 0:
        sum1 += i
print(sum1)
