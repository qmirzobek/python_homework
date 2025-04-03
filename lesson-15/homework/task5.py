import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 5. Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.6, color='g', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution')
plt.show()


