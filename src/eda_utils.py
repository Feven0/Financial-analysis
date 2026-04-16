import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_headline_length_stats(df):
    """
    Returns descriptive statistics for headline lengths.
    """
    df['headline_length'] = df['headline'].apply(len)
    return df['headline_length'].describe()

def plot_top_publishers(df, n=20):
    """
    Plots the top n publishers by article count.
    """
    publisher_counts = df['publisher'].value_counts().head(n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=publisher_counts.values, y=publisher_counts.index)
    plt.title(f'Top {n} Most Active Publishers')
    plt.xlabel('Number of Articles')
    plt.ylabel('Publisher')
    plt.show()

def analyze_publication_dates(df):
    """
    Analyzes publication dates and adds date-related columns.
    """
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    return df

def extract_domain(publisher):
    """
    Extracts domain from email-like publisher names.
    """
    if '@' in str(publisher):
        return publisher.split('@')[-1]
    return publisher

def get_top_keywords(df, column='headline', n=20):
    """
    Returns the most frequent keywords in a text column.
    """
    from collections import Counter
    import re

    words = []
    for text in df[column]:
        words.extend(re.findall(r'\w+', text.lower()))
    
    # Filter common stop words (simple list)
    stop_words = set(['the', 'a', 'to', 'in', 'on', 'at', 'for', 'with', 'and', 'is', 'are', 'by', 'of', 'from', 'it', 'its'])
    filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
    
    return Counter(filtered_words).most_common(n)
