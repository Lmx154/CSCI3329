import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(0, 101, size=100)
plt.hist(data, bins=10, color='purple')
plt.title('Histogram of Randomly Generated Numbers')
plt.xlabel('Number Range')
plt.ylabel('Frequency')
plt.show()