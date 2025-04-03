import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2. Sine and Cosine Plot
x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), 'r-', label='sin(x)')
plt.plot(x, np.cos(x), 'b--', label='cos(x)')
plt.xlabel('x')
plt.ylabel('Function value')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid()
plt.show()


