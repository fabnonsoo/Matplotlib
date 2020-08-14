# FILLING AREA ON LINE PLOTS.....

import pandas as pd
from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')

data = pd.read_csv('sodatamedianpay.csv')
ages = data['Ages']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries),
                 interpolate=True, color='green', alpha=0.2, label='Above Avg')        # for salaries above overall_median

plt.fill_between(ages, py_salaries, dev_salaries, where=py_salaries <=
                 dev_salaries, interpolate=True, alpha=0.2, label='Below Avg')          # for salaries below overall_median


# To fill in the Plots between our Python salary and Developers salaries by age...

plt.legend()

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')


plt.tight_layout()
plt.show()
