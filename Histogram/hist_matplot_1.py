import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

bins = [10, 20, 30, 40, 50, 60]   # Customizes our bins to 5, i.e from 10-20|20-30|30-40|40-50|50-60

# plt.hist(ages, bins=5, edgecolor='black')             # Runs without our customized bins
plt.hist(ages, bins=bins, edgecolor='black')          # Runs with our customized bins


plt.legend()

plt.xlabel('Ages')
plt.ylabel('Total Respondent')
plt.title('Respondent Ages')

plt.tight_layout()
plt.show()
