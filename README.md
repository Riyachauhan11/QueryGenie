# QueryGenie

QueryGenie is an AI-powered customer support automation system that categorizes incoming queries and emails, analyzes sentiment, and generates AI-driven responses based on confidence scores and the urgency or intensity of emotions detected in customer requests.

# 📁 Project Structure
```
📂 QueryGenie
 ├── 📂 data  # Contains datasets for classification & sentiment analysis
 │   ├── emails.csv  # Customer support intent dataset (for query classification)
 │   ├── sentiment_data.csv  # IMDB sentiment dataset (for sentiment analysis)
 │   ├── responses.json  # Predefined fallback responses for LLM failures
 │
 ├── 📂 models  # Pre-trained models for classification & sentiment analysis
 │   ├── email_classifier.pkl
 │   ├── sentiment_analyzer.pkl
 │   ├── vectorizer_email.pkl
 │   ├── vectorizer_sentiment.pkl
 │
 ├── 📂 src  # Core system logic
 │   ├── 📂 training  # Scripts for training ML models
 │   │   ├── train_classifier.py
 │   │   ├── train_sentiment.py
 │   ├── sentiment_analysis.py  # Performs sentiment analysis on queries
 │   ├── classification.py  # Categorizes emails into predefined types
 │   ├── response_generator.py  # Generates AI-based responses
 │   ├── main.py  # Main execution script (Streamlit frontend)
 │
 ├── 📂 tests  # Unit test scripts
 │   ├── test_classification.py
 │   ├── test_sentiment.py
 │   ├── test_response.py
 │
 ├── .env  # Stores API keys (Groq API Key required)
 ├── .gitignore  # Specifies ignored files
 ├── README.md  # Project documentation
 ├── requirements.txt  # Lists required dependencies
```


# 🛠️ Setup Instructions  

## 1️⃣ Clone the Repository  

First, clone this repository to your local machine:  

```bash
git clone https://github.com/Riyachauhan11/QueryGenie.git
cd QueryGenie
```

---

## 2️⃣ Install Dependencies  

Ensure you have **Python 3.8+** installed. Then, install the required dependencies:  

```bash
pip install -r requirements.txt
```

🔹 **(Optional) Using a Virtual Environment:**  
If you prefer **isolating dependencies**, set up a virtual environment:  

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## 3️⃣ Set Up Environment Variables  

This project uses **Groq's Llama model** for AI-generated responses. You need an API key from **[GroqCloud](https://groq.com/)**:  

🔹 **Steps to Get Groq API Key:**  
1. **Sign up** at **[GroqCloud](https://groq.com/)** and log in.  
2. **Navigate to API Keys** in your account settings.  
3. **Generate a new API key** and copy it.  
4. **Create a `.env` file** in the project root and add:  

   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

🚨 **Note:** Do not push `.env` to GitHub for security reasons.  

---

## 4️⃣ Include Datasets in the `data` Folder  

Ensure the `data` folder contains the necessary datasets for **email classification** and **sentiment analysis**:  

🔹 **Customer Query Classification Dataset:**  
Used to categorize customer queries into predefined types.  
📌 [Download from Kaggle](https://www.kaggle.com/datasets/scodepy/customer-support-intent-dataset)  

🔹 **Sentiment Analysis Dataset:**  
Used to analyze if a customer's email sentiment is positive or negative.  
📌 [Download from Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)  

💾 **Steps:**  
1. Download both datasets as **CSV files**.  
2. Place them inside the **`data`** folder following the project structure.  

Even though responses are generated using an **LLM**, a fallback mechanism **`responses.json`** has also been set up. It contains predefined responses to be used when the LLM faces issues generating responses.  

---

## 5️⃣ Training Models (Optional)  

If the pre-trained models (`email_classifier.pkl`, `sentiment_analyzer.pkl`) do not load or crash, retrain them using the scripts in the `src/training` folder:  

```bash
python src/training/train_classifier.py  # Train email classification model
python src/training/train_sentiment.py  # Train sentiment analysis model
```

This will regenerate the `.pkl` model files in the `models` directory.  

---

## 6️⃣ Run Tests in PowerShell  

To ensure everything works correctly, run unit tests before launching the project:  

```bash
cd tests
python test_classification.py  # Test email classification
python test_sentiment.py       # Test sentiment analysis
python test_response.py        # Test response generation
```

If all tests pass, proceed to the next step.  

---

## 7️⃣ Running the Project  

The frontend is built using **Streamlit**. To launch the app:  

```bash
cd src
streamlit run main.py
```

This will start the application and open the **QueryGenie UI** in your browser, where you can enter customer queries and receive AI-generated responses.  

---
