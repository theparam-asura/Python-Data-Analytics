import math
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

predicted_price = 2.50
volatility = 0.15

simulated_price = np.random.normal(predicted_price,volatility,10000)

cost_basis = 2.55

scenerio_profits = simulated_price - cost_basis

ev = np.mean(scenerio_profits)

prob_of_loss = np.mean(scenerio_profits < 0)*100
average_loss = np.mean(scenerio_profits[scenerio_profits<0])

print("Trade Evaluation Reports")
print(f"The expected value of trade is {ev:.4f}$ per unit")
print(f"The probability of loss is {prob_of_loss:.2f}")
print(f"the average loss of trade is {average_loss:.4f}$ per unit")
if ev > 0 :
    print("Positve EV Decision : Recomended Trade")
else:
    print("EV Negative Decision Trade result in loss")