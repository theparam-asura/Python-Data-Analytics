import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import date
import matplotlib.pyplot as plt


# ---------- File Path ----------
baseDir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(baseDir,"Nat_Gas.csv")


# ---------- Load Data ----------
gasData = pd.read_csv(csv_file)

gasData['Dates'] = pd.to_datetime(gasData['Dates'], format='%m/%d/%y')
gasData = gasData.sort_values('Dates')
gasData = gasData.reset_index(drop=True)


# convert dates to ordinal (needed for regression)
gasData['ordDate'] = gasData['Dates'].apply(lambda d : d.toordinal())

X_data = gasData[['ordDate']].values
y_data = gasData['Prices'].values


# ---------- Trend Model ----------
trendModel = LinearRegression()
trendModel.fit(X_data , y_data)

gasData['trend_val'] = trendModel.predict(X_data)
gasData['resid'] = gasData['Prices'] - gasData['trend_val']
gasData['month'] = gasData['Dates'].dt.month


# ---------- Seasonality ----------
seasonalMean = gasData.groupby('month')['resid'].mean()
residStd = gasData['resid'].std()


# ---------- Pricing Function ----------
def getGasPrice(inputDate , returnCI=False):

    lastDate = gasData['Dates'].max()
    maxAllowedDate = lastDate + pd.DateOffset(years=1)

    if pd.Timestamp(inputDate) > maxAllowedDate:
        raise ValueError("Only forecast up to 1 year beyond historical data.")

    ord_val = np.array([[inputDate.toordinal()]])
    trendPart = trendModel.predict(ord_val)[0]

    seasonPart = seasonalMean.get(inputDate.month , 0)

    est_price = trendPart + seasonPart

    if returnCI:
        lower_ci = est_price - 1.96 * residStd
        upper_ci = est_price + 1.96 * residStd
        return est_price , lower_ci , upper_ci

    return est_price



# ---------- Quick Test ----------
testDate = date(2025 , 8 , 31)

pred , low , high = getGasPrice(testDate , returnCI=True)

print("Estimated Price:", round(pred ,2))
print("95% CI:", round(low,2) , "to", round(high,2))


# ---------- Forecast Plot ----------
forecastRange = pd.date_range(
    start = gasData['Dates'].min(),
    end   = gasData['Dates'].max() + pd.DateOffset(years=1),
    freq  = 'ME'
)

forecastList = []

for d in forecastRange:
    forecastList.append(getGasPrice(d))


plt.figure(figsize=(10 ,6))
plt.plot(gasData['Dates'], gasData['Prices'], label="Historical")
plt.plot(forecastRange , forecastList , '--' , label="Forecast")
plt.legend()
plt.title("Natural Gas Price Forecast")
plt.show()