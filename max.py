max_value = 0
best_x = 0
best_y = 0

for x in range(1, 6):
    for y in range(1, 6):
        value = x ** 3 / 2 ** (x - y)
        if value > max_value:
            max_value = value
            best_x, best_y = x, y

print(f'max_value={max_value},max_x={best_x},max_y={best_y}')
