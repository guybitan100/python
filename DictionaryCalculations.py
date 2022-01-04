stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.38,
    'AMZN': 306.21,
    'AAPL': 99.76
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
