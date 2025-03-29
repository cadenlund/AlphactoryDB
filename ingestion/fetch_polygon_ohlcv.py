import os
from dotenv import load_dotenv
from polygon import RESTClient
import pandas as pd
from tqdm import tqdm

load_dotenv()
API_KEY = os.getenv("POLYGON_API_KEY")
client = RESTClient(API_KEY)

def fetch_daily_bars(ticker: str, start: str, end: str):
    results = []

    for bar in client.list_aggs(
        ticker=ticker,
        multiplier=1,
        timespan="day",
        from_=start,
        to=end,
        limit=5000
    ):
        results.append({
            "ticker": ticker,
            "date": pd.to_datetime(bar.timestamp, unit='ms'),
            "open": bar.open,
            "high": bar.high,
            "low": bar.low,
            "close": bar.close,
            "volume": bar.volume
        })

    return pd.DataFrame(results)

def fetch_for_multiple_tickers(tickers, start, end):
    all_dfs = []

    for ticker in tqdm(tickers, desc="Fetching tickers"):
        df = fetch_daily_bars(ticker, start, end)
        all_dfs.append(df)

    return pd.concat(all_dfs, ignore_index=True)

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "TSLA"]
    start_date = "2024-01-01"
    end_date = "2024-03-01"

    df = fetch_for_multiple_tickers(tickers, start_date, end_date)
    print(df.head())

    # Save to CSV (optional)
    df.to_csv("data/daily_ohlcv.csv", index=False)

