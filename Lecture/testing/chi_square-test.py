from scipy.stats import chi2_contingency as chi2
import numpy as np
import pandas as pd

# # Observed values (O)
# df = pd.DataFrame({
#     'Languages': ['Python', 'Java', 'C++'],
#     'CS': [30, 10, 10],
#     'Non-CS': [10, 20, 20]
# })

# df['Total'] = df[['CS', 'Non-CS']].sum(axis=1)
# df.loc['Total'] = df[['CS', 'Non-CS']].sum(axis=0)

# df = df.fillna(0)
# print(df)

# Observed frequence table
# Rows: CS, Non-CS
# Columns: Python, Java, C++
observed = np.array([
    [30, 10, 10],  # CS
    [10, 20, 20]   # Non-CS
])

# Perform Chi-Square test
chi2_stat, p_value, dof, expected = chi2(observed)

# Display the results
print("Chi-Square Test of Independence")
print("-------------------------------")
print(f"Chi-Square Statistic = {chi2_stat:.4f}")
print(f"Degrees of Freedom   = {dof}")
print(f"P-Value              = {p_value:.4f}")
print("Expected Frequencies:")
print(expected)

# Interpretation at 0.05 significance level
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant association between the variables.")
else:
    print("Fail to reject the null hypothesis: No significant association between the variables.")
