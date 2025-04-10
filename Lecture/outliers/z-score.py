import numpy as np
import pandas as pd

data = np.array([10, 12, 14, 15, 18, 21, 22, 25, 28, 30, 2, -10])

mean = np.mean(data)
df = pd.DataFrame(data, columns=['Data'])
# print(df.describe())
std_dev = df['Data'].describe()['std']
print(f"Mean: {mean:.2f}, Standard Deviation: {std_dev:.2f}")
z_scores = (data - mean) / std_dev
for i, j in zip(data, z_scores):
    print(f"Z_{i} = {j:.2f}")

outliers_z = data[np.abs(z_scores) > 1]
print(f"Outliers: {outliers_z}")

# Mild Outliers ranges from |Z| < -2 and |Z| > 2
# Strict Outliers ranges from |Z| < -3 and |Z| > 3
