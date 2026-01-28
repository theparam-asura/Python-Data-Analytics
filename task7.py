import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Taking arguements for monte carlo  simulation

start_price = 255
Time = 252
mu = 0.05
sigma = 0.20
no_of_simulations = 100

#Creating storage & setting first price
sim_paths = np.zeros((Time + 1 , no_of_simulations))
sim_paths[0]=start_price

#Running Simulation & Calculating drift and shock
for t in range(1,Time+1):
    z = np.random.standard_normal(no_of_simulations)
    dt = 1/Time
    drift = (mu - 0.5 * sigma**2) * dt
    shock = sigma*np.sqrt(dt)*z


    sim_paths[t] =sim_paths[t-1] * np.exp(drift+shock)


# Visualization

plt.figure(figsize=(10,6))
plt.plot(sim_paths)
plt.title(f'Monte Carlo Simulation: {no_of_simulations} Random Paths for Natural Gas')
plt.xlabel('Days')
plt.ylabel('Price$')
plt.legend()
plt.show()


#Print
final_prices =sim_paths[-1]
print(f"Average Predicted Price in 1 Year: ${np.mean(final_prices):.2f}")
print(f"Worst Case Scenario (Min): ${np.min(final_prices):.2f}")
print(f"Best Case Scenario (Max): ${np.max(final_prices):.2f}")