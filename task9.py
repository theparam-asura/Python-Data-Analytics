import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Give parameters
strike_price = 50.00
premium = 2.00

#Getting differnet spot price
spot_prices = np.arange(20,81,1)

#Calcualting gross payoff
gross_payoff = np.maximum(spot_prices - strike_price,0)

#Calculating net profit
net_profit = gross_payoff - premium

#Visualization
plt.figure(figsize=(10,6))
plt.plot(spot_prices,net_profit,label='Long Call Option (Profit/Loss)',color='green',linewidth=2)


plt.axhline(0, color='black', linestyle='--', alpha=0.5, label='Break-even Line') # Zero profit line
plt.axvline(strike_price, color='red', linestyle=':', label=f'Strike Price (${strike_price})')

plt.fill_between(spot_prices, net_profit, 0, where=(net_profit > 0), color='green', alpha=0.1)
plt.fill_between(spot_prices, net_profit, 0, where=(net_profit < 0), color='red', alpha=0.1)

# Labels
plt.title(f'Call Option Profit Profile (Strike=${strike_price}, Premium=${premium})')
plt.xlabel('Market Price of Asset ($)')
plt.ylabel('Profit / Loss ($)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
