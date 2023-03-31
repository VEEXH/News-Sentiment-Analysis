import os
import json
import argparse
import requests
import spacy
from bs4 import BeautifulSoup
from transformers import pipeline
from collections import defaultdict

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Perform detailed sentiment analysis on news articles.')
    parser.add_argument('url', help='URL of the news article to analyze')
    return parser.parse_args()

def scrape_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = ' '.join([p.get_text() for p in soup.find_all('p')])
        return content.strip()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch the content from the URL. {e}")
        return None

def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    processed_text = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
    return processed_text

def analyze_emotions(text):
    emotion_analyzer = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-emotion")

    # Split the text into chunks of 500 tokens (to stay within the model's limits)
    max_tokens = 500
    text_chunks = [text[i:i + max_tokens] for i in range(0, len(text), max_tokens)]

    # Analyze emotions for each text chunk and aggregate the results
    aggregated_results = []
    for chunk in text_chunks:
        results = emotion_analyzer(chunk)
        aggregated_results.extend(results)

    # Calculate average scores for each emotion
    emotion_counts = defaultdict(float)
    emotion_sums = defaultdict(float)
    for result in aggregated_results:
        label = result['label']
        score = result['score']
        emotion_counts[label] += 1
        emotion_sums[label] += score

    averaged_results = {label: emotion_sums[label] / emotion_counts[label] for label in emotion_counts}

    # Get the emotion with the highest average score
    top_emotion = max(averaged_results, key=averaged_results.get)

    return top_emotion

def analyze_aspect_based_sentiment(text):
    aspect_analyzer = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    # Split the text into chunks of 500 tokens (to stay within the model's limits)
    max_tokens = 500
    text_chunks = [text[i:i + max_tokens] for i in range(0, len(text), max_tokens)]

    # Analyze sentiment for each text chunk and aggregate the results
    aggregated_results = []
    for chunk in text_chunks:
        results = aspect_analyzer(chunk)
        aggregated_results.extend(results)

    # Calculate average scores for each sentiment
    sentiment_counts = defaultdict(float)
    sentiment_sums = defaultdict(float)
    for result in aggregated_results:
        label = result['label']
        score = result['score']
        sentiment_counts[label] += 1
        sentiment_sums[label] += score

    averaged_results = {label: sentiment_sums[label] / sentiment_counts[label] for label in sentiment_counts}

    # Get the sentiment with the highest average score
    top_sentiment = max(averaged_results, key=averaged_results.get)

    return top_sentiment


def named_entity_recognition(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def main():
    args = get_parsed_arguments()
    url = args.url
    print(f"Scraping content from {url}")

    content = scrape_content(url)
    if content:
        processed_text = preprocess_text(content)
        emotion = analyze_emotions(processed_text)
        sentiment = analyze_aspect_based_sentiment(processed_text)
        entities = named_entity_recognition(processed_text)

        report = {
            "url": url,
            "emotion": emotion,
            "sentiment": sentiment,
            "named_entities": entities
        }

        print("\nGenerated Report:")
        for key, value in report.items():
            print(f"{key}: {value}")

        # Write the report to a JSON file
        output_filename = "generated_report.json"
        with open(output_filename, "w") as outfile:
            json.dump(report, outfile, indent=4, ensure_ascii=False)
        print(f"\nReport saved as {output_filename}")

if __name__ == "__main__":
    main()

