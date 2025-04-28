from statsmodels.stats.proportion import proportions_ztest
from scipy import stats
# Group 1: 50 conversions out of 200 visits
# Group 2: 65 conversions out of 220 visits
conv_rate = [50, 65]
samples = [200, 220]
z_stat, p_value = proportions_ztest(conv_rate, samples)
print(f"Z-statistic: {z_stat:.4f}, P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: No significant difference in conversion rates.")

# t-test
# Sample data: Revenue per user
group_a = [2.1, 2.5, 1.8, 2.4, 2.0, 2.3, 1.9]
group_b = [2.5, 2.7, 2.8, 2.6, 2.9, 2.4, 2.7]
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=True)
print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in revenue per user.")
else:
    print("Fail to reject the null hypothesis: No significant difference in revenue per user.")
