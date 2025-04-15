from scipy import stats

alpha = 0.05
sample_data = [12, 15, 14, 10, 13, 14, 15, 16, 14, 13]
population_mean = 13

t_stat_one, p_value_one = stats.ttest_1samp(sample_data, population_mean)
print("One-sample t-test:")
print(f"T-statistic = {t_stat_one:.4f}")
print(f"P-value = {p_value_one:.4f}")

if p_value_one < alpha:
    print("Conclusion: Reject the null hypothesis. There is a significant differ")
else:
    print("Conclusion: Fail to reject the null hypothesis. No significant differ")

g1 = [23, 21, 19, 24, 25]
g2 = [27, 29, 26, 30, 28]
t_stat_two, p_value_two = stats.ttest_ind(g1, g2, equal_var=True)
print("Two-sample t-test (Independent samples, equal variance):")
print(f"T-statistic = {t_stat_two:.4f}")
print(f"P-value = {p_value_two:.4f}")

if p_value_two < alpha:
    print("Conclusion: Reject the null hypothesis. There is a significant differ")
else:
    print("Conclusion: Fail to reject the null hypothesis. No significant differ")
