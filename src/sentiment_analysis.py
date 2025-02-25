import pickle
import numpy as np

# Load sentiment analysis model
with open("../models/sentiment_analyzer.pkl", "rb") as file:
    model = pickle.load(file)

# Load vectorizer for sentiment analysis
with open("../models/vectorizer_sentiment.pkl", "rb") as file:
    vectorizer = pickle.load(file)

def analyze_sentiment(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]

    # Get probability scores
    proba = model.predict_proba(text_vec)[0]
    confidence = np.max(proba)  # Highest probability score

    return prediction, confidence

if __name__ == "__main__":
    review = "The service was terrible. I want a refund."
    sentiment, confidence = analyze_sentiment(review)
    print(f"Sentiment: {sentiment} (Confidence: {confidence:.2f})")
