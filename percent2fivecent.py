score = float(input("Enter your score: "))
degree = 'EEEEEEDCBAA'
if score > 100 or score < 0:
    print("Invalid score")
else:
    i = int(score // 10)
    print(degree[i])
