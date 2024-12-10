d = {'姓名': '小明', '数学': 56, '英语': 68, '物理': 50.5}
# sum1 = 0
# for i, j in d.items():
#     if isinstance(j, (int, float)):
#         sum1 += j
# d['总分'] = sum1
d['总分'] = sum(j for i, j in d.items() if isinstance(j, (int, float)))
print(d)
