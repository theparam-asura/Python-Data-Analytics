import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import date
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "Nat_Gas.csv")





df = pd.read_csv(file_path)
df['Dates'] = pd.to_datetime(df['Dates'], format='%m/%d/%y')
df.sort_values('Dates', inplace=True)
df.reset_index(drop=True, inplace=True)


df['Ordinal_Date'] = df['Dates'].apply(lambda x: x.toordinal())

X = df[['Ordinal_Date']].values
y = df['Prices'].values

trend_model = LinearRegression()
trend_model.fit(X, y)

df['Trend'] = trend_model.predict(X)
df['Residual'] = df['Prices'] - df['Trend']
df['Month'] = df['Dates'].dt.month

seasonal_adjustments = df.groupby('Month')['Residual'].mean()
residual_std = df['Residual'].std()

def get_gas_price(input_date, return_ci=False):
    max_hist_date = df['Dates'].max()
    max_forecast_date = max_hist_date + pd.DateOffset(years=1)

    if pd.Timestamp(input_date) > max_forecast_date:
        raise ValueError("Forecast beyond 1-year horizon not supported.")

    ordinal_val = np.array([[input_date.toordinal()]])
    trend_prediction = trend_model.predict(ordinal_val)[0]
    seasonal_component = seasonal_adjustments.get(input_date.month, 0)

    prediction = trend_prediction + seasonal_component

    if return_ci:
        lower = prediction - 1.96 * residual_std
        upper = prediction + 1.96 * residual_std
        return prediction, lower, upper

    return prediction

test_date = date(2025, 8, 31)

price, lower, upper = get_gas_price(test_date, return_ci=True)

print(f"Estimated Price for {test_date}: ${price:.2f}")
print(f"95% Confidence Interval: ${lower:.2f} to ${upper:.2f}")

forecast_dates = pd.date_range(
    start=df['Dates'].min(),
    end=df['Dates'].max() + pd.DateOffset(years=1),
    freq='ME'
)

forecast_prices = [get_gas_price(d) for d in forecast_dates]

plt.figure(figsize=(10,6))
plt.plot(df['Dates'], df['Prices'], label='Historical Prices')
plt.plot(forecast_dates, forecast_prices, linestyle='--', label='Forecast')
plt.legend()
plt.show()
