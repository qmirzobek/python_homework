import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 8. Stacked Bar Chart
time_periods = ['T1', 'T2', 'T3', 'T4']
category_a = [10, 20, 30, 40]
category_b = [15, 25, 35, 45]
category_c = [20, 30, 40, 50]
plt.figure()
plt.bar(time_periods, category_a, label='Category A')
plt.bar(time_periods, category_b, bottom=category_a, label='Category B')
plt.bar(time_periods, category_c, bottom=np.array(category_a) + np.array(category_b), label='Category C')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()
