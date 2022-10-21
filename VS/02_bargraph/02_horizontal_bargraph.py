import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np
import csv

df = pd.read_csv('C:\\Users\\saish\\python_modules\\VS\\02_bargraph\\data.txt',sep = ',',index_col='Responder_id')
print(df.head())