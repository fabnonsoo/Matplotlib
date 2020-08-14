import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')


data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='inferno',
            edgecolors='black', alpha=0.65, linewidths=1.5)

cbar = plt.colorbar()
cbar.set_label('Likes/Dislikes Ratio')

plt.xscale('log')
plt.yscale('log')


plt.title('Trending Youtube Videos')

plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()
plt.show()
