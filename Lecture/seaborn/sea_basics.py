import matplotlib.pyplot as plt

categories = ["Furniture", "Office Supplies", "Technology"]
profit = [14390.45, 3450.50, 12340.80]
sales = [80000, 23000, 90000]

plt.figure(figsize=(8, 5))
plt.plot(categories, sales, marker='o')
plt.title("Sales Trend over Categories")
plt.xlabel("Categories")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, profit)
plt.title("Average Profit by Category")
plt.xlabel("Categories")
plt.ylabel("Profit")

for bar, value in zip(bars, profit):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 100, f'{value:.2f}', ha='center')

plt.show()
