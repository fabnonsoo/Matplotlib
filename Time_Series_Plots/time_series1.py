# 'linestyle' includes a straight line between the data points
# The 'gcf' in 'plt.gcf().autofmt_xdate()' means 'get current figure'
# gca: 'get current access' in 'plt.gca().xaxis.set_major_formatter()'
# '%b, %d %Y' format string means month, day and year...
# With 'inplace=True' we don't need to do:- 'data = data.sort('Date', inplace=True)


import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='dashed')

plt.gcf().autofmt_xdate()                      # Automatically Slants the dates on the x-axis...

date_format = mpl_dates.DateFormatter('%b %d, %Y')

plt.gca().xaxis.set_major_formatter(date_format)         # Formats our date to May 30, 2019....
plt.tight_layout()

plt.show()
