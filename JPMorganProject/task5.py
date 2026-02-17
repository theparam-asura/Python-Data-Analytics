import math
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

# mu, sigma = 0, 0.1 # mean and standard deviation
# s = np.random.normal(mu, sigma, 1000)
# print("check")

data =yf.download("NG=F", start="2022-01-01")




predicted_price = 2.50
volatility = 0.15

simulated_price = np.random.normal(predicted_price,volatility,10000)

plt.figure(figsize=(10,6))
plt.hist(simulated_price,bins=100,color='royalblue',alpha=0.7)
plt.axvline(predicted_price,color='red',linestyle='dashed',label='Mean Price')
plt.title('Distribution of 10000 Potential Natural Gas Prices')
plt.xlabel('Possible Price($)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

prob_above = np.mean(simulated_price> 2.70)*100
print(f"There is a {prob_above: .2f}% chance the price will exceed $2.70")
