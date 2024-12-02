from random import shuffle

teacher = ['teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5', 'teacher6', 'teacher7', 'teacher8', 'teacher9']
office = [[], [], []]
shuffle(teacher)
office[0] = teacher[:3]
office[1] = teacher[3:6]
office[2] = teacher[6:]
print(office)
