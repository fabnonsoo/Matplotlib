# Median JavaScript Developers Salaries By Age.....

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48950, 54000, 57657, 63366, 66125, 70003, 70000, 72435, 75968, 85020]
plt.plot(ages_x, py_dev_y, color='#5a7d9a', linestyle='-',
         marker='o', linewidth=3, label='Python_Devs')


js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JS_Devs')


dev_y = [41675, 43000, 47500, 51345, 54750, 57850, 64100, 66980, 69450, 73567, 77789]
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')


plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
