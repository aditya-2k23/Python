import numpy as np
import matplotlib.pyplot as plt

data = np.array([10, 12, 14, 15, 18, 21, 22, 25, 28, 2, -10])

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print("Q1:", q1, "Q3:", q3, "IQR:", iqr)
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("Lower Bound:", lower, "Upper Bound:", upper)

outliers_iqr = data[(data < lower) | (data > upper)]
print("Outlier:", outliers_iqr)

plt.figure(figsize=(6, 4))
plt.boxplot(data, vert=False)
plt.xlabel("Values")
plt.title('Box Plot for Outlier Detection')
plt.show()
