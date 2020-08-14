# 's' argument stands for changing the size of the data points on a scatter plot...
# 'marker' argument helps depict the we want our points to be seen on the plot..
# 'c' argument stands for color
# 'cmap' stands for color maps - It's used to set colors on our markers/data points...
# 'cbar/color bar' is used to show the legend on the chart....


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x = [4, 2, 7, 6, 5, 4, 8, 3, 4, 6, 8, 1, 6, 2, 7, 9, 6, 4, 5, 3]
y = [5, 3, 9, 7, 4, 2, 7, 8, 1, 3, 2, 6, 4, 7, 5, 9, 1, 7, 4, 1]

# Colors corresponds with the x & y axis...
colors = [9, 5, 2, 7, 2, 5, 1, 5, 7, 9, 3, 7, 1, 7, 5, 2, 8, 5, 6, 7]
sizes = [239, 209, 394, 486, 538, 381, 228, 315, 436,
         273, 153, 399, 255, 174, 191, 501, 293, 539, 436, 397]

# plt.scatter(x, y, s=50, c=colors, cmap='Greens', edgecolors='black', alpha=0.65, linewidths=1.5)         # used w/out 'sizes'
plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolors='black', alpha=0.65, linewidths=1.5)

cbar = plt.colorbar()
cbar.set_label('Satisfaction')


plt.tight_layout()
plt.show()
