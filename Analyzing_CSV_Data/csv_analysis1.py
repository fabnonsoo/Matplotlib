# Analyzing Data Loaded from CSV File: Using an 'import csv' module
# NB: 'from collections import Counter' is used when a data is too large to loop through....

import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Using csv:
with open('sodata_19.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)                        # Prints only the first row of csv_reader
    print(row)                                    # O/p the full dict values of the 1st row of the csv file
    print(row['LanguageWorkedWith'])              # O/p only the 'LanguageWorkedWith' dict values of 1st row...
    print(row['LanguageWorkedWith'].split(';'))   # Gives a Python list of the 'LanguageWorkedWith'
