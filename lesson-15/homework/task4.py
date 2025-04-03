import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 4. Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c=np.random.rand(100), marker='o', alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')
plt.grid()
plt.show()
