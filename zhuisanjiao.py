# method 1
for i in range(1,8,2):
    print(('*'*i).center(7))
for i in range(5,0,-2):
    print(('*'*i).center(7))

# method 2
for i in range(1,5):
    for j in range(4-i,0,-1):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
for i in range(3,0,-1):
    for j in range(4-i,0,-1):
        print(' ',end='')
    for k in range(2*i,1,-1):
        print('*',end='')
    print()

# method 3
for i in range(1,5):
    for j in range(4-i,0,-1):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
for i in range(1,4):
    for j in range(i):
        print(' ',end='')
    for k in range(7-2*i,0,-1):
        print('*',end='')
    print()

# method 4
for i in range(4):
    print(' '*(3-i),end='')
    print('*'*(2*i+1))
for i in range(2,-1,-1):
    print(' '*(3-i),end='')
    print('*'*(2*i+1))

