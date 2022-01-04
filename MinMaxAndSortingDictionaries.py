stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.38,
    'AMZN': 306.21,
    'AAPL': 99.76
}
# The first to zip is the value because we need to sort it
names = zip(stocks.values(), stocks.keys())

for a, b in names:
    print(a, b)
# Get max of the values
print(max(stocks.values()))
# Get max of the values with the key
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))