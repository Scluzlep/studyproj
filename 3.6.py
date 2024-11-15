for i in range(40):
    if i % 3 == 0 or i % 10 == 3 or i // 10 == 3:
        continue
    else:
        print(i,end=' ')