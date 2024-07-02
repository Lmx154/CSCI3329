import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(50)
y1 = np.random.rand(50)
x2 = np.random.rand(50)
y2 = np.random.rand(50)

plt.scatter(x1, y1, color='blue', marker='o', label='Distribution 1')
plt.scatter(x2, y2, color='red', marker='o', label='Distribution 2')

plt.title('Scatter Plot with Two Distributions')
plt.xlabel('Random x values')
plt.ylabel('Random y values')
plt.legend()
plt.show()