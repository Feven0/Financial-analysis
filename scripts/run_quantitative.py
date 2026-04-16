import sys
import os
import pandas as pd

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_stock_data
from src.indicators import calculate_moving_averages, calculate_rsi, calculate_macd

def main():
    print("Loading stock data...")
    stock_folder = os.path.join('data', 'raw', 'yfinance_data', 'Data')
    
    # Analyze AAPL as an example
    ticker = 'AAPL'
    df = load_stock_data(stock_folder, ticker)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    print(f"\n--- Technical Analysis for {ticker} ---")
    
    # Calculate Indicators
    df = calculate_moving_averages(df)
    df = calculate_rsi(df)
    df = calculate_macd(df)

    print("\nRecent TA Data:")
    print(df[['Close', 'SMA_20', 'SMA_50', 'RSI', 'MACD']].tail(10))

    # Save results
    os.makedirs('results', exist_ok=True)
    df.to_csv(f'results/{ticker}_indicators.csv')
    print(f"\nResults saved to results/{ticker}_indicators.csv")

if __name__ == "__main__":
    main()
