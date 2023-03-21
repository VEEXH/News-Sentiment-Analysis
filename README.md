# News Sentiment Analysis

This Python script fetches news data from the News API, filters articles based on user preferences and keywords, and performs basic sentiment analysis on the article titles.
Features

    Fetches news data from a news API and performs sentiment analysis on the articles.
    Filters articles based on user preferences and keywords.
    Handles API response status codes and filtering articles.
    Allows users to search for articles based on their interests and preferences.
    Communicates the results in a user-friendly format.

## Requirements

    Python 3.6 or higher
    requests library
    textblob library
    News API key

To install the required libraries, run:

pip install requests textblob

Usage

    Replace your_news_api_key_here in the script with your News API key.

python

API_KEY = "your_news_api_key_here"

    Run the script:

python news_sentiment_analysis.py

    Enter a keyword related to your interest when prompted:

css

Enter a keyword related to your interest: technology

    The script will fetch articles related to the keyword and display their titles, sentiment, and URLs.
