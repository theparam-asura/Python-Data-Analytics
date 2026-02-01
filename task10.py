import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def get_quant_data(ticker, start_date):
    """
    Downloads historical data and calculates daily log returns.
    
    Parameters:
        ticker (str): The stock symbol (e.g., 'NG=F')
        start_date (str): Format 'YYYY-MM-DD'
        
    Returns:
        pd.DataFrame: Cleaned data with a 'Log_Ret' column.
    """
    # 1. Download
    print(f"Fetching data for {ticker}...")
    df = yf.download(ticker, start=start_date, progress=False)
    
    # 2. Check for empty data
    if df.empty:
        raise ValueError(f"No data found for {ticker}. Check internet or symbol.")
    
    # 3. Calculate Returns (The logic from Day 2)
    # Using 'Close' price. We use .copy() to avoid SettingWithCopy warnings
    df = df.copy()
    df['Log_Ret'] = np.log(df['Close'] / df['Close'].shift(1))
    
    # 4. Drop NaN values created by the shift
    df.dropna(inplace=True)
    
    print("Data processing complete.")
    return df

def run_simulation_check(data):
    """
    Runs a quick Monte Carlo check (Day 7 logic) to verify math libraries.
    """
    last_price = float(data['Close'].iloc[-1])
    volatility = float(data['Log_Ret'].std() * np.sqrt(252))
    
    print(f"Current Price: {last_price:.2f}")
    print(f"Annualized Volatility: {volatility:.2%}")
    
    # Quick Simulation
    simulation = np.random.normal(last_price, volatility, 1000)
    print(f"Simulated Mean Price: {np.mean(simulation):.2f}")
    print("Math libraries: OK")

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    try:
        # Test with Natural Gas
        gas_data = get_quant_data("NG=F", "2024-01-01")
        run_simulation_check(gas_data)
        
        print("\nSUCCESS: System Ready for J.P. Morgan Task 1.")
        
    except Exception as e:
        print(f"\nFAILURE: {e}")

