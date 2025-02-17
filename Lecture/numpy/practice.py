import numpy as np

# Create a 2D NumPy array to represent purchase amounts for a month (30 days)
# arr = np.random.randint(1, 200, size=(5, 30))  # 5 customers, 30 days
# print("Purchase amounts:\n", arr)

# # Compute the total spending of each customer over the month
# total_spending = np.sum(arr, axis=1)
# print("Total spending of each customer:", total_spending)

# # Find the average daily spending per customer
# average_spending = np.mean(arr, axis=1)
# print("Average daily spending per customer:", average_spending)

# # Find customers who spent more than $3000
# high_spenders = np.where(total_spending > 3000)[0]
# print("Customers who spent more than $3000:", high_spenders)

"""
Question: Stock Market Data Analysis
A financial company tracks daily stock prices of multiple companies in a 2D NumPy array, where each
row represents a stock and each column represents daily closing prices. The company wants to analyze
stock trends and risks.
Problem Statement:
Using NumPy, perform the following stock market analysis:
1. Create a 2D NumPy array to store stock prices.
2. Find the maximum and minimum prices for each stock.
3. Compute the cumulative sum of each stock .
4. Sort stocks based on average return

arr = np.random.randint(1, 100, size=(5, 10))
print(arr)

print("\nMax")
print(np.max(arr, axis=1))
print("\nMin")
print(np.min(arr, axis=1))

print("\nCumulative Sum")
print(np.cumsum(arr, axis=1))

print("\nSorted Stocks based on Average Return")
avg = np.mean(arr, axis=1)
indexes = np.argsort(avg)
print(arr[indexes])

"""
