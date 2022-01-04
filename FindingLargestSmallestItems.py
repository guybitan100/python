import heapq

grades = [30, 43, 654, 34, 132, 66, 99, 532]
# GET 3 THE LARGES IN THE LIST
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'GOOG', 'price': 520.54},
    {'ticker': 'FB', 'price': 76.45},
    {'ticker': 'YHOO', 'price': 39.38},
    {'ticker': 'AMZN', 'price': 306.21},
    {'ticker': 'AAPL', 'price': 99.76}
]
# All item in the list is map
'''
for item in stocks:
    print(item)
'''
print(heapq.nlargest(2, stocks, key=lambda stock: stock['price']))
