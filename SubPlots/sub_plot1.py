# SubPlots are used to work with plots in a object oriented matter...
# SubPlots are used to replace 'gcf' & 'gca' when plotting/working w/multiple figures & axis...
# By default, SubPlots creates a figure & specifies a certain number of rows & columns of axis....
# NB: 'sharex=True' removes the x-axis values for the 1st Plot (i.e All_Devs)


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('sodatamedianpay.csv')
ages = data['Ages']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


# fig, ax = plt.subplots()                        # Prints the default plots...

# To get the Python & JavaScript plots on one plot, we add more axis (ax)--> Prints the SubPlots...
# That is it makes the 2 plots be on one figure (see Line 17);
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

# print(ax1)
# print(ax2)

ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')


ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')                         # Commenting this line removes label of x-axis..
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')     # Commenting this line removes title from ax2..
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
