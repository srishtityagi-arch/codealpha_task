stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total = 0

while True:
    stock = input("Enter Stock Name (or done): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter Quantity: "))
        total += stocks[stock] * qty
    else:
        print("Stock not found!")

print("Total Investment =", total)