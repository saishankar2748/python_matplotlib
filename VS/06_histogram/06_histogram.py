import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('C:\\Users\\saish\\python_modules\VS\\06_histogram\\data.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins=bins,edgecolor='black',log=True)



median_age = 29
color = '#fc4f30'
plt.axvline(median_age,color=color,label='Age_median',linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.savefig('C:\\Users\\saish\\python_modules\VS\\06_histogram\\06-histogram')
plt.show()