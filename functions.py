from transformers import pipeline
from datetime import datetime, timedelta, timezone
import pandas as pd
import yfinance as yf


def fetch_news_articles(ticker, days_back):
    pipe = pipeline("text-classification", model="ProsusAI/finbert")

    stock = yf.Ticker(ticker)
    raw = stock.news or []

    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)

    filtered = []
    for item in raw:
        content = item.get("content", {}) or {}

        pubdate_str = content.get("pubDate")
        published_dt = _parse_pubdate(pubdate_str) if pubdate_str else None
        if not published_dt:
            continue
        if published_dt < cutoff:
            continue

        filtered.append({
            "Title": content.get("title"),
            "Summary": content.get("summary"),
            "Link": (content.get("canonicalUrl") or {}).get("url") or (content.get("clickThroughUrl") or {}).get("url") or content.get("previewUrl"),
            "Published": published_dt.isoformat()
        })

    return filtered, pipe


def summarize_articles(articles, pipe):
    data_list = []
    total_score = 0.0
    num_articles = 0

    for a in articles:
        text = (a.get("Summary") or a.get("Title") or "").strip()
        if not text:
            continue

        sentiment = pipe(text)[0]

        data_list.append({
            "Title": a.get("Title"),
            "Link": a.get("Link"),
            "Published": a.get("Published"),
            "Label": sentiment["label"],
            "Sentiment": sentiment["score"],
        })

        if sentiment["label"].lower() == "positive":
            total_score += sentiment["score"]
            num_articles += 1
        elif sentiment["label"].lower() == "negative":
            total_score -= sentiment["score"]
            num_articles += 1

    df = pd.DataFrame(data_list)
    avg_score = total_score / num_articles if num_articles > 0 else 0
    return df, avg_score
