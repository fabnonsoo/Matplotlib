# This lines of code makes the 2 plots in "sub_plot1.py" file to be on two different figures instead of one;

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('sodatamedianpay.csv')
ages = data['Ages']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


# Making the two Plots on two figures...;
All_Devs, ax1 = plt.subplots()
py_js, ax2 = plt.subplots()


ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')


ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()


# To save the Plots...;
All_Devs.savefig('All_Devs.png')
py_js.savefig('py_js.png')
