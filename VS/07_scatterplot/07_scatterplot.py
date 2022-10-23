import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('C:\\Users\\saish\\python_modules\\VS\\07_scatterplot\\2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.scatter(view_count, likes,c=ratio, cmap='summer',
             edgecolor='black',linewidths=1,alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.savefig('C:\\Users\\saish\\python_modules\\VS\\07_scatterplot\\07_scatterplot')
plt.show()