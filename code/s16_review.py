import yfinance as yf       # yahoo finance:  python -m pip install yfinance

# stock = yf.Ticker('AAPL')
# info = stock.info            # a dict!
# print(type(info))

# print(info.keys())
# print(len(info))
# print(info['shortName'])
# print(info['longName'])
# print(info['currentPrice'])

# print(info['longBusinessSummary'])

# print('iphone' in info['longBusinessSummary'].lower().split())

# print(info['city'])
# info['city'] [0] = 'c'
# info['city'] = 'Wellesley'
# print(info['city'])


# tickers = ['AAPL', 'NVDA', 'MSFT']
# prices = {}
# for t in tickers:
#     prices[t] = yf.Ticker(t).info['currentPrice']

# print(prices)

# print(sorted(prices)) #create a new list of the keys in prices, sorted alphabetically
# print(sorted(prices.values()))
# print(sorted(prices.values(), reverse=True)) #create a new list of the values in prices, sorted from largest to smallest
# print(tickers)

# how to sort stocks by values, but still show k: v?
print(sum(prices.values()))

prices = {'AAPL': 173.57, 'NVDA': 280.35, 'MSFT': 305.22}

total = 0
for price in prices.values():
    total += price
print(total)

tickers.append('GOOG')
print(tickers)
# tickers = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']
print(prices)



tickers = ['AAPL', 'NVDA', 'MSFT']
stocks = {} #{'NVDA': [open, currentPrice, volume}]

for t in tickers:
    #stocks[t] = yf.Ticker(t).info['open'], yf.Ticker(t).info['currentPrice'], yf.Ticker(t).info['volume']
    #stocks[t] = (yf.Ticker(t).info['open'], yf.Ticker(t).info['currentPrice'], yf.Ticker(t).info['volume']) #create a tuple of the three values
    info_list = {}
    for name in ['open', 'currentPrice', 'volume']:
        info_list[name] = yf.Ticker(t).info[name]
    stocks[t] = info_list
print(stocks)

stocks['AAPL']['currentPrice']=260
print(stocks) #Dictionaries are mutable, so we can change the value at a specific key.




