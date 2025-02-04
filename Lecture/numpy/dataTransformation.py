"""
You are working as a data analyst for a company that deals with large datasets. Your team receives a 2D NumPy array containing customer transaction data, where each row represents a different customer, and columns represent transaction amounts in different months.

Using Numpy functions:
    - Find the maximum, minimum, and total transaction amount across all customers.
    - Compute the cumulative sum of transactions column-wise.
    - Flatten the 2D array into a 1D array and sort the transactions in ascending order.
    - Transform the dataset by reshaping it into a different stricture.
Write Python code to achieve these tasks and explain the significance of each function in data transformation.

# Sample transaction data (4 customers, 5 months)
"""

import numpy as np

transaction_data = np.array([
    [100.0, 200.0, 300.0, 400.0, 500.0],
    [150.0, 250.0, 350.0, 450.0, 550.0],
    [200.0, 300.0, 400.0, 500.0, 600.0],
    [250.0, 350.0, 450.0, 550.0, 650.0]
])

max_transaction = np.max(transaction_data)
min_transaction = np.min(transaction_data)
total_transaction = np.sum(transaction_data)

print("Maximum transaction amount:", max_transaction)
print("Minimum transaction amount:", min_transaction)
print("Total transaction amount:", total_transaction)

cumulative_sum = np.cumsum(transaction_data, axis=0)
print("Cumulative sum of transactions column-wise:")
print(cumulative_sum)

flattened_data = transaction_data.flatten()
sorted_transactions = np.sort(flattened_data)
print("Sorted transactions in ascending order:")
print(sorted_transactions)

reshaped_data = transaction_data.reshape(5, 4)
print("Reshaped transaction data:")
print(reshaped_data)
