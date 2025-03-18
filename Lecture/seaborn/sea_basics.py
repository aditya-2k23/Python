import seaborn as sb
import matplotlib.pyplot as plt

categories = ["Furniture", "Office Supplies", "Technology"]
profit = [14390.45, 3450.50, 12340.80]
sales = [80000, 23000, 90000]

sb.set(style="whitegrid")
# "darkgrid", "whitegrid", "dark", "white", "ticks"

#1. Line Plot - Sales Trend over Categories
plt.figure(figsize=(8, 5))
sb.lineplot(x=categories, y=sales)
plt.title("Sales Trend over Categories")
plt.show()

#2. Bar Plot - Average Profit by Category
plt.figure(figsize=(8, 5))
barplot = sb.barplot(x=categories, y=profit, errorbar=None)
plt.title("Average Profit by Category")

for i, value in enumerate(profit):
    barplot.text(i, value + 100, f'{value:.2f}', ha='center')
plt.show()

#3. Scatter Plot - Sales vs Profit
plt.figure(figsize=(8, 5))
sb.scatterplot(x=sales, y=profit)
plt.title("Sales vs Profit")
plt.show()

#4. Heatmap - Correlation between Sales and Profit
import numpy as np
import pandas as pd

data = pd.DataFrame({
    "Sales": sales,
    "Profit": profit,
})
plt.figure(figsize=(6, 4))
corr = data.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap between Sales and Profit")
plt.show()
