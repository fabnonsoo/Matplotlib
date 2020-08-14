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

for item in language_counter.most_common(15):          # Seperates the results from the list of--> 'print(language_counter.most_common(15))'
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)
