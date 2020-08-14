# Stack Plots are useful when you want to track the total and see the breakdown of that total by a specific category.
# The 'loc/location' in the legend moves the position of the legend to where you want to place it(in this case: uppeer left)..

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#e5ae37', '#fc4f30']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)


plt.title('My Stack Plot')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
