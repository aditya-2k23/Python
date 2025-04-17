import math
from scipy.stats import norm

# Input parameters
sample_mean = 169.5
population_mean = 168
population_std_dev = 3.9
sample_size = 36
alpha = 0.05
tail = "two"

# Calculate the standard error
standard_error = population_std_dev / math.sqrt(sample_size)

# Calculate the z-score
z_score = (sample_mean - population_mean) / standard_error

# Calculate the p-value based on the tail type
if tail == "two":
    p_value = 2 * (1 - norm.cdf(abs(z_score)))
elif tail == "left":
    p_value = norm.cdf(z_score)
elif tail == "right":
    p_value = 1 - norm.cdf(z_score)
else:
    raise ValueError("Tail must be 'two', 'left', or 'right'")

# Determine the conclusion
if p_value < alpha:
    conclusion = "Reject the null hypothesis"
else:
    conclusion = "Fail to reject the null hypothesis"

# Print the results
print(f"Sample Mean: {sample_mean}")
print(f"Population Mean: {population_mean}")
print(f"Population Standard Deviation: {population_std_dev}")
print(f"Sample Size: {sample_size}")
print(f"Alpha: {alpha}")
print(f"Tail: {tail}")
print(f"Standard Error: {standard_error:.4f}")
print(f"Z-Score: {z_score:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Conclusion: {conclusion}")
