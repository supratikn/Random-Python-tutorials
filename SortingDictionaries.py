stocks = {
    'GOOG': 520.24,
    'FB': 76.45,
    'YHOO': 39.28,
    'APL': 99.78
}


answer =zip(stocks.values(),stocks.keys())

print(min(answer))
print(sorted(zip(stocks.keys(),stocks.values())))