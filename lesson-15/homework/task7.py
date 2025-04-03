import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 7. Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.figure()
plt.bar(products, sales, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()
