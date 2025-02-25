import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("data/emails.csv")
X_train = df["email"]
y_train = df["category"]

# Train TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save the trained model and vectorizer
with open("models/email_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer_email.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully!")
