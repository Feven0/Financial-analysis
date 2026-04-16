from textblob import TextBlob
import pandas as pd

def get_sentiment_score(text):
    """
    Calculates sentiment score for a given text.
    Returns: polarity (-1 to 1).
    """
    if not isinstance(text, str):
        return 0
    return TextBlob(text).sentiment.polarity

def apply_sentiment_analysis(df, column='headline'):
    """
    Applies sentiment analysis to a dataframe column.
    """
    df['sentiment'] = df[column].apply(get_sentiment_score)
    return df

def aggregate_daily_sentiment(df):
    """
    Aggregates sentiment scores by date.
    """
    # Ensure date is just date
    df['date_only'] = pd.to_datetime(df['date']).dt.date
    return df.groupby('date_only')['sentiment'].mean().reset_index()
