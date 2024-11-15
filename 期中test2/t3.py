time1 = input('输入坐车的时间（24小时制）')
mile = int(input('输入坐车的里程'))
if 7 <= int(time1) < 22:
    start_fee = 5
    next_fee = 2
else:
    start_fee = 6
    next_fee = 3
if 0 < mile <= 3:
    total_fee = start_fee
else:
    total_fee = start_fee + next_fee * (mile - 3)
print(total_fee)
