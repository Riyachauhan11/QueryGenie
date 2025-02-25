from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd

# Load dataset
df = pd.read_csv("data/sentiment_data.csv")  
X = df["review"] 
y = df["sentiment"]

# Train model
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X)
model = LogisticRegression()
model.fit(X_train, y)

# Save model
with open("models/sentiment_analyzer.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer_sentiment.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Sentiment model trained and saved!")
