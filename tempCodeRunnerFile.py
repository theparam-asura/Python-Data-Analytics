import math
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np


data =yf.download("NG=F", start="2022-01-01")
# print(data.head())


#Step 1
last_date = data.index[-1]

#Step 2
future_date = pd.date_range(
    start= last_date + pd.Timedelta(days=1),
    freq='D',
    periods=30
)

#Step 3
x_hist = np.arange(len(data))
y_hist = data['Close'].to_numpy().ravel()

#Step 4
m, c = np.polyfit(x_hist, y_hist, 1)
m=float(m)
c=float(c)

#Step 5
x_future =np.arange(len(data),len(data)+30)

#Step 6
y_future = m*x_future + c

#Step 7
print(f"Current Trend (Slope): {m:.6f} USD/Day")


#Step 8
print(f"Price Prediction for {future_date[-1].date()}: ${y_future[-1]:.2f}")

#Step 9
plt.plot(data.index,y_hist,label="Historical")
plt.plot(
    future_date,
    y_future,
    label='Extrapolated',
    linestyle='--'
)

#Step 10
plt.legend()
plt.show()