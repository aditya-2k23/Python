from scipy.stats import chi2_contingency as chi2
import numpy as np

# Observed values (O)
# Rows: A1, A2, A3
# Columns: B1, B2, B3
observed = np.array([
    [35, 52.5, 12.5],
    [28.1, 42.1, 9.8],
    [6.9, 10.4, 2.7]
])

chi2_stat, p_value, dof, expected = chi2(observed)

print("Chi-Square Test of Independence")
print("-------------------------------")
print(f"Chi-Square Statistic = {chi2_stat:.4f}")
print(f"Degrees of Freedom   = {dof}")
print(f"P-Value              = {p_value:.4f}")
print("Expected Frequencies:")
print(expected)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant association between the variables.")
else:
    print("Fail to reject the null hypothesis: No significant association between the variables.")
