import matplotlib.pyplot as plt

categories = ["Furniture", "Office Supplies", "Technology"]
profit = [14390.45, 3450.50, 12340.80]
sales = [80000, 23000, 90000]

# Line plot for Sales Trend over Categories
plt.figure(figsize=(8, 5))
plt.plot(categories, sales, marker='o')
plt.title("Sales Trend over Categories")
plt.xlabel("Categories")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar plot for Average Profit by Category
plt.figure(figsize=(8, 5))
barplot = plt.bar(categories, profit, color='skyblue')
plt.title("Average Profit by Category")
plt.xlabel("Categories")
plt.ylabel("Profit")

for i, value in enumerate(profit):
    plt.text(i, value + 100, f'{value:.2f}', ha='center')
plt.show()
