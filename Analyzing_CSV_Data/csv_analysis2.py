# To update and count the list of LanguageWorkedWith, we use 'Counter'....
# This is because the number of responses from LanguageWorkedWith is > 87000 & too large to loop through...


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

print(language_counter)                              # Prints out all languagesworkedwith...
print(language_counter.most_common(15))              # Prints most 15 languagesWorkedWith...
