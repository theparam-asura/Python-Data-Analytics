import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Creating parts of dataframe dictionaries value
month = ['Jan','Feb','Mar','Apr','May','June']
contango_prices = [2.50,2.55,2.62,2.70,2.80,2.95]
backwardation_prices = [4.00,3.80,3.50,3.20,2.90,2.70]

#Creating dataframe
df = pd.DataFrame({
    'Months': month,
    'Contango_curve' : contango_prices,
    'Backwardation_curve' : backwardation_prices
})

# Print dataframe
print(df)


#Calculation of profit and loss
contango_profit = df['Contango_curve'].iloc[-1] - df['Contango_curve'].iloc[0]
backwardation_loss = df['Backwardation_curve'].iloc[-1] - df['Backwardation_curve'].iloc[0]


#Print profit and loss
print(f"\nScenario A (Contango) Spread: ${contango_profit:.2f} (Profit from Buying Now & Selling Later)")
print(f"Scenario B (Backwardation) Spread: ${backwardation_loss:.2f} (Loss from Buying Now & Selling Later)")

#Visualization
plt.figure(figsize=(10,6))

#print using seaborn
sns.lineplot(x='Months',y='Contango_curve',data=df,markers='o',label='Contango Price Store Gas', color='green')
sns.lineplot(x='Months', y='Backwardation_curve', data=df, marker='o', label='Backwardation (Sell Immediately)', color='red')


plt.title('The Future Term Strcutre :When to buy when to sell')
plt.xlabel('Delivery Month')
plt.ylabel('Price $')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()