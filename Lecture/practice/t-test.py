from scipy import stats

group_a = [23, 43, 58, 69]
group_b = [12, 42, 96, 103]

t, p = stats.ttest_ind(group_a, group_b, equal_var=True)
print(f"{t:.4f}")
print(f"{p:.4f}")

alpha = 0.05
if p < alpha:
    print("Rejected")
else:
    print("Accepted")
