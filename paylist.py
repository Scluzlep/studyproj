with open('购物单.txt','r',encoding='utf-8') as f:
    s1 = f.readlines()
    total_price = 0
    for i in s1:
        per_price = float(i.split(' ')[1])
        per_num = float(i.split(' ')[2])
        per_sum_price = per_price * per_num
        total_price += per_sum_price
    print('{:.2f}'.format(total_price))
