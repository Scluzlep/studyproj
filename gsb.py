num = int(input("Enter a number: "))
for i in range(1,num):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        break
else:
    print(f'{num}内没有3和5的公倍数')