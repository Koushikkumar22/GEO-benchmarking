import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

def extract_mentions(response_text, competitors):
    """Return list of (brand, sentiment_score, position_weight)."""
    mentions = []
    words = response_text.split()
    for brand in competitors:
        pattern = re.compile(rf"\b{brand}\b", re.IGNORECASE)
        matches = list(pattern.finditer(response_text))
        for idx, match in enumerate(matches):
            # position weighting
            weight = 2 if idx == 0 else 1
            # sentiment
            sentiment = sia.polarity_scores(match.group())
            if sentiment["compound"] >= 0.05:
                sentiment_weight = 1.0
            elif sentiment["compound"] <= -0.05:
                sentiment_weight = 0.25
            else:
                sentiment_weight = 0.5
            mentions.append((brand, sentiment_weight, weight))
    return mentions

def calculate_sov(responses, competitors):
    scores = {c: 0 for c in competitors}
    for text in responses:
        for brand, sent_w, pos_w in extract_mentions(text, competitors):
            scores[brand] += sent_w * pos_w
    total = sum(scores.values())
    sov = {c: (scores[c] / total * 100 if total > 0 else 0) for c in competitors}
    return scores, sov