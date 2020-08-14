# PLOTTING THE DATA FOR THE MOST POPULAR PROGRAMMING USED BY DEVELOPERS - Using the 'import csv' module.....
# NB: 'from collections import Counter' is used when a data is too large to loop through....


import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Using csv:
with open('sodata_19.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguageWorkedWith'].split(';'))


languages = []
popularity = []

for item in language_counter.most_common(15):          # Seperates the results from the list of--> 'print(language_counter.most_common(15))' for Plotting...
    languages.append(item[0])
    popularity.append(item[1])


languages.reverse()                              # Prints the results in descending order..
popularity.reverse()                             # Prints the results in descending order..

plt.barh(languages, popularity)                   # The 'barh' O/p a horinzontal chart

plt.xlabel('Number of People Who Use')
plt.ylabel('Programming Languages')
plt.title('Most Popular Languages')

plt.tight_layout()

plt.show()
