import matplotlib.pyplot as plt

x, y = [], []
with open('9.4 dos.csv', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.strip().split(',')
        x.append(float(data[0]))
        y.append(float(data[1]))

plt.plot(x, y, color='black', marker='o', linestyle='-', linewidth=1, label='dos')
plt.savefig('dos.png')
plt.show()
