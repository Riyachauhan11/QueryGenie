import pickle
import numpy as np

# Load trained model
with open("../models/email_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("../models/vectorizer_email.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Function to classify email with confidence score
def classify_email(email_text):
    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]
    
    proba = model.predict_proba(email_vec)[0]
    confidence = np.max(proba) 

    return prediction, confidence

if __name__ == "__main__":
    sample_email = "My order is late. Where is my package?"
    category, confidence = classify_email(sample_email)
    print(f"Predicted Category: {category} (Confidence: {confidence:.2f})")
