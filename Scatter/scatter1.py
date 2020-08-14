# SCATTER PLOTS are used when you want to show the relationship between 2 sets of values to see if they correlate....
# SCATTER PLOTS are really good for seeing different kind of trends...


import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('seaborn')

x = [4, 2, 7, 6, 5, 4, 8, 3, 4, 6, 8, 1, 6, 2, 7, 9, 6, 4, 5, 3]
y = [5, 3, 9, 7, 4, 2, 7, 8, 1, 3, 2, 6, 4, 7, 5, 9, 1, 7, 4, 1]

plt.scatter(x, y, s=50, c='red', edgecolors='black', alpha=0.65, linewidths=1.5)


plt.tight_layout()
plt.show()
