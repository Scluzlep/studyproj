for i in range(1, 101):
    if i % 7 == 0 or str(i).find('7') != -1:
        print('*', end=' ')
    else:
        print(i, end=' ')
