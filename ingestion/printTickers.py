from polygon import RESTClient
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("POLYGON_API_KEY")
client = RESTClient(API_KEY)

tickers = []
for t in client.list_tickers(
	market="stocks",
	active="true",
	order="asc",
	limit="100",
	sort="ticker",
	):
    tickers.append(t)

print(tickers)


client = RESTClient("YOUR_API_KEY")

tickers = []
for t in client.list_tickers(
	market="stocks",
	active="true",
	order="asc",
	limit="100",
	sort="ticker",
	):
    tickers.append(t)

print(tickers)

