for i in range(1, 5):
    for j in range(4 - i, 0, -1):
        print(' ', end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print()
for i in range(3, 0, -1):
    for j in range(4 - i, 0, -1):
        print(' ', end='')
    for j in range(2 * i, 1, -1):
        print('*', end='')
    print()
