import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')


data = pd.read_csv('C:\\Users\\saish\\python_modules\\VS\\08_plotting_time_series\\data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date',inplace=True)
price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date,price_close,linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('C:\\Users\\saish\\python_modules\\VS\\08_plotting_time_series\\08_time_series')
plt.show()