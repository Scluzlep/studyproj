import random

end_num = random.randint(20,30)
flag = 1
s = 0
for i in range(1,end_num+1):
    q = 1 / i
    s = s + q
print('{:.3f}'.format(s))
