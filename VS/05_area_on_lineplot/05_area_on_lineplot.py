import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('C:\\Users\\saish\\python_modules\\VS\\05_area_on_lineplot\\data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages,py_salaries,dev_salaries,
                where=(py_salaries>dev_salaries),
                interpolate=True,alpha=0.25,label='above avg' )

plt.fill_between(ages,py_salaries,dev_salaries,
                where=(py_salaries<=dev_salaries),
                interpolate=True,color='red',alpha=0.25, label = 'below avg' )


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig('C:\\Users\\saish\\python_modules\\VS\\05_area_on_lineplot\\05-area_on_lineplot')
plt.show()