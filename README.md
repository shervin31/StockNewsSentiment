# StockNewsSentiment 📈

A Python tool that analyzes news sentiment for stocks using NLP and real-time news data.

## Features
- 📰 Fetches financial news from NewsAPI
- 🤖 Analyzes sentiment using FinBERT (financial NLP model)
- 📊 Returns sentiment scores and article details
- ⏳ Customizable date ranges

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/StockNewsSentiment.git
cd StockNewsSentiment
```

2. Install dependencies:
pip install transformers requests pandas

4. Get a NewsAPI key:
Go to newsapi.org and sign up for a free account

Get your API key from the dashboard

Open functions.py and replace the API_KEY:
API_KEY = "your_actual_api_key_here"  # Replace this string

Usage
Run the main script:
python main.py

Example interaction:
Enter a stock/company to search news for: Apple
Enter number of days to look back: 7
Average sentiment score: 0.68

Output
DataFrame with columns: Title, Link, Published, Label, Sentiment

Average sentiment score (-1 to 1 scale)

Dependencies
transformers - For FinBERT NLP model pipeline
requests - For API calls to NewsAPI
pandas - For data manipulation

Project Structure
StockNewsSentiment/
├── functions.py
├── main.py
└── README.md

How It Works
Fetches news from NewsAPI

Processes text with FinBERT model

Calculates aggregate sentiment scores

Requirements
Python 3.7+

NewsAPI key

Internet connection

Disclaimer
For informational purposes only. Not financial advice. 
