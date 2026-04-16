import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_news_data
from src.eda_utils import get_headline_length_stats, plot_top_publishers, analyze_publication_dates, extract_domain, get_top_keywords

def main():
    print("Loading data...")
    news_path = os.path.join('data', 'raw', 'news_data', 'raw_analyst_ratings.csv')
    df = load_news_data(news_path)

    print("\n--- Descriptive Statistics ---")
    stats = get_headline_length_stats(df)
    print(stats)

    print("\n--- Publisher Analysis ---")
    publisher_counts = df['publisher'].value_counts().head(10)
    print(publisher_counts)

    print("\n--- Keyword Extraction (Topic Modeling) ---")
    top_keywords = get_top_keywords(df, n=15)
    for word, count in top_keywords:
        print(f"{word}: {count}")

    print("\n--- Domain Analysis ---")
    df['domain'] = df['publisher'].apply(extract_domain)
    top_domains = df['domain'].value_counts().head(10)
    print(top_domains)

    print("\n--- Time Series Analysis ---")
    df = analyze_publication_dates(df)
    df['date_only'] = df['date'].dt.date
    daily_counts = df.groupby('date_only').size()
    print(f"Top 5 Peak Publication Days:\n{daily_counts.sort_values(ascending=False).head(5)}")

    # Save a plot
    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title('Daily Publication Frequency')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/daily_publication_plot.png')
    print("\nPlot saved to results/daily_publication_plot.png")

if __name__ == "__main__":
    main()
