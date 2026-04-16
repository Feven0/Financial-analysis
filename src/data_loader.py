import pandas as pd
import os

def load_news_data(file_path):
    """
    Loads news data from a CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

def load_stock_data(folder_path, ticker):
    """
    Loads stock data for a specific ticker.
    """
    file_path = os.path.join(folder_path, f"{ticker}.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)
