import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_news_data, load_stock_data
from src.indicators import calculate_moving_averages, calculate_rsi, calculate_macd
from src.sentiment import apply_sentiment_analysis, aggregate_daily_sentiment
from src.correlation import calculate_stock_returns, merge_news_stock, calculate_correlation

def main():
    print("Step 1: Loading Data...")
    news_path = os.path.join('data', 'raw', 'news_data', 'raw_analyst_ratings.csv')
    stock_folder = os.path.join('data', 'raw', 'yfinance_data', 'Data')
    
    news_df = load_news_data(news_path)
    aapl_df = load_stock_data(stock_folder, 'AAPL')

    print("\nStep 2: Processing Stock Data (AAPL)...")
    aapl_df['Date'] = pd.to_datetime(aapl_df['Date'])
    aapl_df = calculate_moving_averages(aapl_df)
    aapl_df = calculate_rsi(aapl_df)
    aapl_df = calculate_macd(aapl_df)
    aapl_df = calculate_stock_returns(aapl_df)

    print("\nStep 3: Processing News Sentiment (AAPL)...")
    # Filter for AAPL specific news
    aapl_news = news_df[news_df['stock'] == 'AAPL'].copy()
    print(f"Found {len(aapl_news)} articles for AAPL.")
    
    aapl_news = apply_sentiment_analysis(aapl_news)
    daily_sentiment = aggregate_daily_sentiment(aapl_news)

    print("\nStep 4: Correlation Analysis...")
    merged_df = merge_news_stock(daily_sentiment, aapl_df)
    
    if len(merged_df) > 0:
        corr = calculate_correlation(merged_df)
        print(f"Correlation between Sentiment and Daily Returns: {corr:.4f}")
        
        # Save plot
        plt.figure(figsize=(10, 6))
        sns.regplot(x='sentiment', y='returns', data=merged_df)
        plt.title('AAPL: Sentiment vs Daily Returns Correlation')
        os.makedirs('results', exist_ok=True)
        plt.savefig('results/aapl_sentiment_correlation.png')
        print("Correlation plot saved to results/aapl_sentiment_correlation.png")
    else:
        print("No overlapping dates found for correlation analysis.")

    # Save final dataset
    merged_df.to_csv('results/aapl_final_analysis.csv', index=False)
    print("Final results saved to results/aapl_final_analysis.csv")

if __name__ == "__main__":
    main()
