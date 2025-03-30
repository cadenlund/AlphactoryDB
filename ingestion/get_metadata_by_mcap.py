import os
import time
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from polygon import RESTClient
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load API key
load_dotenv()
client = RESTClient(os.getenv("POLYGON_API_KEY"))

# Step 1: Get all common stock tickers
def get_all_common_stock_tickers():
    logging.info("📡 Fetching ticker list from Polygon...")
    tickers = []
    try:
        for t in client.list_tickers(
            market="stocks",
            type="CS",
            active=True,
            sort="ticker",
            limit=1000
        ):
            tickers.append(t.ticker)
        logging.info(f"✅ Total tickers fetched: {len(tickers)}\n")
    except Exception as e:
        logging.error(f"❌ Failed to get tickers: {e}")
    return tickers

# Step 2: Get metadata for one ticker
def get_metadata(ticker):
    try:
        r = client.get_ticker_details(ticker)
        return {
            "ticker": r.ticker,
            "active": r.active,
            "type": r.type,
            "market_cap": r.market_cap,
            "primary_exchange": r.primary_exchange,
            "sic_description": r.sic_description,
            "list_date": r.list_date,
            "name": r.name,
            "description": r.description,
            "total_employees": r.total_employees,
            "share_class_shares_outstanding": r.share_class_shares_outstanding,
            "weighted_shares_outstanding": r.weighted_shares_outstanding
        }
    except Exception as e:
        logging.warning(f"⚠️  {ticker}: {e}")
        return None

# Step 3: Build the stock metadata universe
def build_universe():
    start_time = time.time()

    tickers = get_all_common_stock_tickers()
    if not tickers:
        logging.error("❌ No tickers fetched. Exiting.")
        return

    logging.info("📦 Fetching metadata for each ticker...")
    records = []
    for ticker in tqdm(tickers, desc="📥 Getting details", ncols=100):
        data = get_metadata(ticker)
        if data and data["market_cap"]:
            records.append(data)

    logging.info(f"✅ Metadata retrieved for {len(records)} tickers with valid market cap")

    df = pd.DataFrame(records)
    logging.info("🧹 Filtering by exchange and type...")

    before_filter = len(df)
    df = df[df["primary_exchange"].isin(["XNYS", "XNAS"])]
    df = df[df["type"] == "CS"]
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors="coerce")
    df = df.dropna(subset=["market_cap"])

    logging.info(f"✅ Filtered {before_filter} ➡️ {len(df)} tickers after cleaning")

    df = df.sort_values("market_cap", ascending=False)
    logging.info("🏆 Top stocks by market cap selected")

    os.makedirs("data", exist_ok=True)
    output_path = "data/stock_metadata.csv"
    df.to_csv(output_path, index=False)
    logging.info(f"💾 Saved metadata to ➜ {output_path}")

    elapsed = round(time.time() - start_time, 2)
    logging.info(f"⏱️ Completed in {elapsed} seconds.")

if __name__ == "__main__":
    build_universe()

