from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Print API key to check if it's set
if not api_key:
    raise ValueError("GROQ_API_KEY is not set! Please set it in your environment.")

# Load predefined responses as fallback
with open("../data/responses.json", "r") as file:
    responses = json.load(file)

# Initialize Groq Llama model
llm = ChatGroq(
    temperature = 0,
    groq_api_key = api_key, 
    model_name = "llama-3.3-70b-versatile"
)

def generate_response(category, email_text):
    """Generates a response using Llama 3.3-70B, with a fallback to predefined responses."""
    try:
        response = llm.invoke(f"Category: {category}\nEmail: {email_text}\nGenerate a response.")
        return response.content.strip()  
    except Exception as e:
        print(f"Llama Model Error: {e}")

    # Fallback to predefined responses if LLM fails
    return responses.get(category, "I'm sorry, I don't understand your request.")

def escalate_to_human(category, category_confidence, sentiment, sentiment_confidence):
    """Determines if a case needs to be escalated to human support."""
    # if the category of email falls into a field that might drive customers away from their
    # platform it's important the query be forwarded to human agent when sentiment is negative as well
    if category in ["REFUND"] and sentiment == "negative":
        return True
    if category_confidence < 0.6 or sentiment_confidence < 0.5:
        return True  
    return False

# Example usage
if __name__ == "__main__":
    category = "REFUND"
    email_text = "I ordered a product, but it arrived damaged. I want a full refund."
    print(generate_response(category, email_text))
