from functions import fetch_news_articles, summarize_articles

def main():
    ticker = input("Enter a stock ticker (e.g., AAPL, TSLA): ").strip().upper()
    days = int(input("Enter number of days to look back: ").strip())

    articles, pipe = fetch_news_articles(ticker, days)
    df, avg_score = summarize_articles(articles, pipe)

    print("\n===== Sentiment Summary =====")
    print(f"Ticker: {ticker}")
    print(f"Articles analyzed: {len(df)}")

    if df.empty:
        print("No articles available.")
        return

    sentiment_counts = df["Label"].value_counts()
    for label, count in sentiment_counts.items():
        print(f"{label.capitalize():<8}: {count}")

    print(f"\nAverage sentiment score: {avg_score:.2f}")

    # OPTIONAL: show only top 3 headlines
    print("\nTop headlines:")
    for title in df["Title"].head(3):
        print(f"- {title}")

if __name__ == "__main__":
    main()

display(df)
