# ANALYZING CSV DATA USING: pandas...


import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Using pandas method: Without '.astype(str)' you'll get traceback of-> AttributeError: 'float' object has no attribute 'split'
data = pd.read_csv('sodata_19.csv')
ids = data['Respondent'].astype(str)
lang_responses = data['LanguageWorkedWith'].astype(str)


language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))


languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])


languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.xlabel('Number of People Who Use')
# plt.ylabel('Programming Languages')
plt.title('Most Popular Languages')

plt.tight_layout()

plt.show()
