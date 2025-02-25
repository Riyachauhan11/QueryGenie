import streamlit as st
from classification import classify_email
from sentiment_analysis import analyze_sentiment
from response_generator import generate_response, escalate_to_human

# Streamlit UI
st.title("📧 QueryGenie")

email_text = st.text_area("✉️ Enter a query below to get it resolved by our AI-Powered Customer Support", "")

if st.button("Process Query"):
    if email_text.strip():
        # Get classification, sentiment, and response
        category, category_confidence = classify_email(email_text)
        sentiment, sentiment_confidence = analyze_sentiment(email_text)
        response = generate_response(category,email_text)

        # Determine if escalation is needed
        escalation_needed = escalate_to_human(category, category_confidence, sentiment, sentiment_confidence)

        # Display Results
        st.write(f"📌 **Category:** {category} (Confidence: {category_confidence:.2f})")
        st.write(f"🔍 **Sentiment:** {sentiment} (Confidence: {sentiment_confidence:.2f})")
        st.write(f"💬 **AI Response:** {response}")

        if escalation_needed:
            st.error("⚠️ This email requires escalation to a human agent!")
        else:
            st.success("✅ AI response is sufficient.")
    else:
        st.warning("Please enter an email before processing.")
