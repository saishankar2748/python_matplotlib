import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

slices = [120,80,30,20]
labels = ['Sixty','Forty','Extra1','Extra2']
colors = ['#008fd5','#fc4f30','#e5ae37','#6d904f']

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}, colors=colors)

plt.title('My Awseme Pie Chart')
plt.tight_layout()
plt.show()



#  Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f