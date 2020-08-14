import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')


data = pd.read_csv('sodataage.csv')
ids = data['Respondent']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#e5ae37'

plt.axvline(median_age, color=color, label='Median Age', linewidth=2.5)       # 'plt.axvline' stands for 'access vertical line'

plt.legend()

plt.xlabel('Ages')
plt.ylabel('Total Respondent')
plt.title('Respondent Ages')

plt.tight_layout()
plt.show()
