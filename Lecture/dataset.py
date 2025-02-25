import pandas as pd
import numpy as np

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", np.nan, "David", "Eve"],
    "Age": [25, np.nan, 30, np.nan, 40],
    "City": ["New York", "Los Angeles", "Chicago", np.nan, "Houston"],
    "Salary": [50000, 60000, np.nan, 80000, 70000]
}

df = pd.DataFrame(data)
print("Original Dataframe with Missing Values:")
print(df)

print("\nMissing values in each column:")
print(df.isnull().sum())

df_dropped_rows = df.dropna()
print("\nDataframe after dropping rows with missing values:")
print(df_dropped_rows)

df_dropped_cols = df.dropna(axis=1)
print("\nDataframe after dropping columns with missing values:")
print(df_dropped_cols)

df_filled = df.fillna({"Age": df["Age"].mean(), "City": "Unknown", "Salary": df["Salary"].median()})
print("\nDataframe after filling missing values:")
print(df_filled)

df_filled = df.ffill()
print("\n After forward fill:")
print(df_filled)

df_bfill = df.bfill()
print("\n After backward fill:")
print(df_bfill)
