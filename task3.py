import math
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
#from datetime import datetime, timedelta
import numpy as np


data =yf.download("NG=F", start="2022-01-01")

#print(data.head())
#pecentage change calculation
# data['Simple Return'] =data['Close'].pct_change
# data['Log Retrun']=np.log(data['Close']/data['Close'].shift(1))
# monthly_volatility=data['Log Retrun'].groupby(data.index.month).std()  #monthly volatility calculation throgh standard deviation
# print("Monthly Volatility:")
# print(monthly_volatility.sort_values(ascending=False))
# print("Simple Return:")
# print(data['Simple Return'])
# print(data['Log Retrun'])

data['SMA21'] = data['Close'].rolling(window=21).mean()
data['SMA252'] = data['Close'].rolling(window =252).mean()


#Visualization

data[['Close','SMA21','SMA252']].plot(figsize=(12,6))
plt.title('Natural gas price : Short term vs Long term ')
plt.show()