import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sentiment_analysis import analyze_sentiment

def test_analyze_sentiment():
    positive_sentiment, positive_confidence = analyze_sentiment("I love this service!")
    negative_sentiment, negative_confidence = analyze_sentiment("This is terrible.")

    assert positive_sentiment == "positive"
    assert negative_sentiment == "negative"

    assert 0.0 <= positive_confidence <= 1.0  
    assert 0.0 <= negative_confidence <= 1.0

if __name__ == "__main__":
    test_analyze_sentiment()
    print("Sentiment analysis tests passed!")
