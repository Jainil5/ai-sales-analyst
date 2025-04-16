import pandas as pd
from transformers import pipeline

def analyze_sentiment(text):

    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0] 

    if result["label"] == "POSITIVE":
        return "Positive"
    elif result["label"] == "NEGATIVE":
        return "Negative"
    else:
        return "Neutral" 

def add_sentiments(df, text_column='review'):
    
    df['sentiment'] = df[text_column].apply(analyze_sentiment)
    return df

if __name__ == '__main__':
    review_data = pd.read_csv('backend/dataset/reviews.csv')

    df_with_sentiment = add_sentiments(review_data)

    print(df_with_sentiment.head())

    df_with_sentiment.to_csv('backend/reviews_with_sentiments.csv', index=False)
