mile = int(input("输入里程: "))
waiting_time = int(input('输入等待时间'))
if mile <= 3:
    fee = 13
else:
    if mile <= 18:
        fee = 13 + 2.3 * (mile - 13)
    else:
        fee = 13 + 2.3 * 15 + 2.3 * 1.5 * (mile - 18)
waiting_fee = waiting_time * 1
total_fee = fee + waiting_fee
print(total_fee)