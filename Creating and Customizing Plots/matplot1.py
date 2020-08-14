# Using matplotlib to analyze the median salary for a developer based on their age

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [41675, 43000, 47500, 51345, 54750, 57850, 64100, 66980, 69450, 73567, 77789]

plt.plot(ages_x, dev_y)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.show()
