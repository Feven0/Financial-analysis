import pandas as pd

def calculate_stock_returns(df, column='Close'):
    """
    Calculates daily percentage change for stock prices.
    """
    df['returns'] = df[column].pct_change()
    return df

def merge_news_stock(news_df, stock_df):
    """
    Merges news sentiment data with stock returns data on date.
    """
    # news_df should be aggregated by date
    # stock_df should have a Date column or index
    
    if 'Date' not in stock_df.columns:
        stock_df = stock_df.reset_index()
    
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
    
    merged = pd.merge(news_df, stock_df[['Date', 'returns']], left_on='date_only', right_on='Date', how='inner')
    return merged

def calculate_correlation(df, col1='sentiment', col2='returns'):
    """
    Calculates Pearson correlation between two columns.
    """
    return df[col1].corr(df[col2])
