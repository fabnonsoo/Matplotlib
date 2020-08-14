# PLOTTING MULTIPLE DATA USING "numpy"

# importing numpy helps us to plot multiple bar charts properly
# 'x_indexes' prevents our bar charts from being stacked onto of each other which isn't nice
# 'width' helps the bars to be seperated properly & can be set at whatever figure..
# plt.xticks(ticks=x_indexes, labels=ages_x) --> helps label our 'Ages' properly(removes it as indexes)


import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.20

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python')

cpp_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, cpp_dev_y, width=width, color='#e5ae38', label='C++')


plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.tight_layout()

plt.show()
