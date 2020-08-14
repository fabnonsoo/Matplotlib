# Write a program that finds out the Data Scientist that works the most on a project in a Data Team..


from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]


datasci_1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
datasci_2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
datasci_3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#e5ae37', '#fc4f30']

plt.stackplot(minutes, datasci_1, datasci_2, datasci_3, labels=labels, colors=colors)

plt.title('My Data Team Contribution Plot')
plt.legend(loc=(0.08, 0.04))                    # Means 7% from left & 5% from bottom
plt.tight_layout()
plt.show()
