lis = [1, 2, 7, 4, 5]
max1 = lis.index(max(lis))
lis.pop(max1 + 1)
lis.insert(max1, 6)
print(lis)
