# StockNewsSentiment 📈

A Python tool that analyzes news sentiment for stocks using NLP and real-time news data.

## Features
- 📰 Fetches financial news from NewsAPI
- 🤖 Analyzes sentiment using FinBERT (financial NLP model)
- 📊 Returns sentiment scores and article details
- ⏳ Customizable date ranges

## Installation

### Clone the repository:
```bash
git clone https://github.com/yourusername/StockNewsSentiment.git
cd StockNewsSentiment
```

## Install Dependencies
```bash
pip install transformers requests pandas
```

## Get a NewsAPI key:
Go to newsapi.org and sign up for a free account
Get your API key from the dashboard
Open functions.py and replace the API_KEY:
```bash
API_KEY = "your_actual_api_key_here"  # Replace this string
```
