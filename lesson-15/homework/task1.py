import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Basic Plotting
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function Plot')
plt.legend()
plt.grid()
plt.show()
