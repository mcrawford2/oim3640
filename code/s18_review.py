import yfinance as yf
from pprint import pprint

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
stocks = {}

for t in tickers:
    stocks[t] = yf.Ticker(t).info['currentPrice']
    #create a dictionary with the the current price of each stock

print(stocks)

print('After sorting...')
print(sorted(stocks))
