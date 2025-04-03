import numpy as np

data = [10, 12, 14, 15, 18, 21, 22, 25, 28, 30, 2, -10]
sort = sorted(data)

q1 = np.percentile(sort, 25)
q3 = np.percentile(sort, 75)
iqr = q3 - q1

print("Q1:", q1, "Q3:", q3, "IQR:", iqr)
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("Lower Bound:", lower, "Upper Bound:", upper)
