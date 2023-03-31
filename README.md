# News Sentiment Analyzer

The News Sentiment Analyzer is a Python script that performs detailed sentiment analysis on news articles. It scrapes the content from a given URL, processes the text, and generates a report containing the overall emotion, sentiment, and named entities in the article.

## Installation

1. Clone the repository:

``git clone https://github.com/VEEXH/News-Sentiment-Analysis.git``
``cd News-Sentiment-Analysis``


2. Create a virtual environment:

``python3 -m venv venv``


3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On Linux/MacOS:

  ```
  source venv/bin/activate
  ```

4. Install the required dependencies:

``pip install -r requirements.txt``


## Usage

Run the script by providing a news article URL as an argument:

``python news_sentiment_analyzer.py https://example.com/news-article``


The script will scrape the content from the URL, preprocess the text, and analyze the emotions, sentiment, and named entities. It will then generate a report and print the results.

## License

This project is licensed under the terms of the MIT License.


