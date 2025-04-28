import numpy as np
from scipy import stats

data = [12.1, 13.4, 13.8, 14.0, 13.9, 13.3, 12.9, 13.7, 13.5, 14.1]
statistic, p_value = stats.shapiro(data)
print(f"Shapiro-Wilk Test Statistic: {statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The data is not normally distributed.")
else:
    print("Fail to reject the null hypothesis: The data is normally distributed.")
