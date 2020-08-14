# Using 'styles' in our plot....

# When we use styles in our plots, we don't really need colors, linewidth and so on...
# We removed 'plt.grid(True)' because some of these styles have their own grid prefeerences in place..
# To see the types of styles available for our plots--> print(plt.style.available)

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
plt.xkcd()                                    # Results in a comic style plot

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48950, 54000, 57657, 63366, 66125, 70003, 70000, 72435, 75968, 85020]
plt.plot(ages_x, py_dev_y, label='Python_Devs')


js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, label='JS_Devs')


dev_y = [41675, 43000, 47500, 51345, 54750, 57850, 64100, 66980, 69450, 73567, 77789]
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')


plt.legend()
plt.tight_layout()
plt.savefig('comicplot.png')                          # Saves the plot...

plt.show()
