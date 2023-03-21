import requests
import json
from textblob import TextBlob

API_KEY = "your_news_api_key_here"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news_data(query_params):
    query_params["apiKey"] = API_KEY
    response = requests.get(BASE_URL, params=query_params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching news data:", response.status_code)
        return None

def filter_articles(articles, keyword):
    filtered_articles = [article for article in articles if keyword.lower() in article["title"].lower()]
    return filtered_articles

def sentiment_analysis(articles):
    for article in articles:
        sentiment = TextBlob(article["title"]).sentiment
        article["sentiment"] = sentiment.polarity
    return articles

def main():
    user_preferences = {
        "language": "en",
        "pageSize": 100,
        "sortBy": "relevancy"
    }

    user_keyword = input("Enter a keyword related to your interest: ").strip()
    
    news_data = fetch_news_data(user_preferences)
    if news_data:
        filtered_articles = filter_articles(news_data["articles"], user_keyword)
        analyzed_articles = sentiment_analysis(filtered_articles)

        print(f"\nTop {len(analyzed_articles)} articles related to '{user_keyword}':\n")
        for article in analyzed_articles:
            print(f"Title: {article['title']}\nSentiment: {'Positive' if article['sentiment'] > 0 else 'Negative' if article['sentiment'] < 0 else 'Neutral'}\nURL: {article['url']}\n")

if __name__ == "__main__":
    main()
