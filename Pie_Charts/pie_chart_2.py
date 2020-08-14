# 'explode' argument offsets the Pie chart, i.e seperates a portion/slice from the others....
# 'shadow' makes the Pie chart look like 3D...
# 'startangle' makes the Pie chart to be rotated a little bit... Rotation starts @ the angle it's set..
# 'autopct/autopercentage' sets the % values of all our items on the Pie....
# The number after the decimal in autopct='%1.1f%%' sets our result in chart to no of decimal places(in this case 1dp).


from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0.1, 0, 0]             # 0.1 means 10% radius of the SQL slice


plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=65, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})


plt.title('My Pie Chart')
plt.tight_layout()
plt.show()
