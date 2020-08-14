# Median Python Developers Salaries By Age.....

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [41675, 43000, 47500, 51345, 54750, 57850, 64100, 66980, 69450, 73567, 77789]

plt.plot(ages_x, dev_y, label='All Devs')
plt.plot(ages_x, dev_y, color='b', linestyle='--', marker='.', label='All Devs')        # default color, linestyle & label


py_dev_y = [45372, 48950, 54000, 57657, 63366, 66125, 70003, 70000, 72435, 75968, 85020]

plt.plot(ages_x, py_dev_y, label='Python_Devs')
plt.plot(ages_x, py_dev_y, color='g', linestyle='-', marker='o', label='Python_Devs')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')


plt.legend(['All Dev', 'Python_Devs'])        # Used when there's no label in 'plt.plot' for dev_y & py_dev_y
plt.legend()                                  # Used when there's a label in 'plt.plot' for dev_y & py_dev_y

plt.show()
