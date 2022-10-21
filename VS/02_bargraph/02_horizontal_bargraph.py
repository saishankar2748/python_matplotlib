import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np

df = pd.read_csv('C:\\Users\\saish\\python_modules\\VS\\02_bargraph\\data.txt',sep = ',')
# print(df.head())

lang_responses = df['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

# print(language_counter)  # returns dictionary of counted values
# print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15): # returns tuple
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()
plt.show()