import seaborn as sb
import matplotlib.pyplot as plt

categories = ["Furniture", "Office Supplies", "Technology"]
profit = [14390.45, 3450.50, 12340.80]
sales = [80000, 23000, 90000]

sb.set(style="whitegrid")

plt.figure(figsize=(8, 5))
sb.lineplot(x=categories, y=sales)
plt.title("Sales Trend over Categories")
plt.show()

plt.figure(figsize=(8, 5))
barplot = sb.barplot(x=categories, y=profit, errorbar=None)
plt.title("Average Profit by Category")

for i, value in enumerate(profit):
    barplot.text(i, value + 100, f'{value:.2f}', ha='center')
plt.show()
