import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3. Subplots
x = np.linspace(0, 5, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, x**3, 'r')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 1].plot(x, np.sin(x), 'g')
axs[0, 1].set_title('f(x) = sin(x)')
axs[1, 0].plot(x, np.exp(x), 'b')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 1].plot(x, np.log(x + 1), 'm')
axs[1, 1].set_title('f(x) = log(x+1)')
plt.tight_layout()
plt.show()


