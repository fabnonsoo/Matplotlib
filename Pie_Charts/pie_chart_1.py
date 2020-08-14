# It isn't best practice to use Pie Chart when you have more than 5 items...
# 'wedgeproperty or wedgeprops' provides a line that seperates different values in the pie chart...
# You can make the slices any number you want. Isn't a must you add up to 100%. Chart will do that for you.


from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [40, 15, 10, 35]   # OR [130, 45, 60, 85, 24]
labels = ['40%', '15%', '10%', '35%']
colors = ['#008fd5', '#6d904f', '#fc4f30', '#e5ae37']   # OR ['blue', 'green', 'red', 'yellow']

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})


plt.title('My Pie Chart')
plt.tight_layout()
plt.show()
