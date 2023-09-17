import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_sentiment_nltk(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    sentiment = get_sentiment(sentiment_scores["compound"])

    analysis_result = {
        "sentiment": sentiment,
        "polarity": sentiment_scores["compound"]
    }

    return analysis_result

def get_sentiment(sentiment_score):
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def generate_star_rating_nltk(sentiment_score):
    if sentiment_score >= 0.4:
        return "⭐️⭐️⭐️⭐️⭐️"
    elif sentiment_score >= 0.2:
        return "⭐️⭐️⭐️⭐️"
    elif sentiment_score >= 0.05:
        return "⭐️⭐️⭐️"
    elif sentiment_score >= -0.05:
        return "⭐️⭐️"
    else:
        return "⭐️"

def generate_star_ratings_for_comments_nltk(comments):
    results = []

    for idx, comment in enumerate(comments):
        newcomm=str(comment)
        result = analyze_sentiment_nltk(newcomm)
        star_rating = generate_star_rating_nltk(result["polarity"])

        comment_result = {
            "comment_text": newcomm,
            "sentiment": result["sentiment"],
            "star_rating": star_rating
        }

        results.append(comment_result)
    return results


def conv(comments:list):
    newlist=[]
    for comment in comments:
        newcom=str(comment)
        newlist.append(newcom)
    return newlist