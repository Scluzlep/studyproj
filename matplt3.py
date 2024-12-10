import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)
y1 = np.sin(x)
y2 = x / (x * x + 2)
y3 = np.tan(x)
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue', marker='o', linestyle='-')
plt.text(-2, 0.8, 'y=sinx')

plt.subplot(2, 2, 3)
plt.plot(x, y2, color='red', marker=',', linestyle=':')
plt.text(1.4, 0.1, 'y=x/x^2+2')

plt.subplot(2, 2, 4)
plt.plot(x, y3, color='red', marker=',', linestyle=':')
plt.text(1.7, 30, 'y=tanx')
plt.show()
