import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classification import classify_email 

def test_email_classification():
    """Tests email classification for different types of queries."""
    
    test_cases = [
        ("I have an issue with my recent order.", ["ORDER"]),
        ("I need a refund for my damaged product.", ["REFUND"]),
        ("My payment was deducted twice. Please help.", ["PAYMENT"]),
        ("Can you provide me invoice for the purchased product?", ["INVOICE"]),
        ("I want to cancel my subscription to newsletter.", ["NEWSLETTER"]),
        ("Thank you for the great service!", ["FEEDBACK"]),
    ]

    for email_text, expected_categories in test_cases:
        category, confidence = classify_email(email_text)
        assert category in expected_categories, f"Unexpected category {category} for input: {email_text}"
        assert 0.0 <= confidence <= 1.0, f"Confidence out of range for input: {email_text}"

    print("Email classification tests passed!")

if __name__ == "__main__":
    test_email_classification()
