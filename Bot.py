from binance.client import Client
import os

api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"

client = Client(api_key, api_secret)
price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"BTC Price: {price['price']}")
