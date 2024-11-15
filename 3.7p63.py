num = int(input("Enter a number: "))
i = num - 1
while 1 < i < num:
    if num % i == 0:
        print(i)
        break
    i = i - 1
