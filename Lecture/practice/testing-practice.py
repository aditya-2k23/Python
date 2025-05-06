import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from scipy import stats

# Set the random seed for reproducibility
np.random.seed(42)

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = [iris.target_names[i] for i in iris.target]

print("First 5 rows of the Iris dataset:")
print(iris_df.head())

# Create a figure with subplots for each distribution
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Different Probability Distributions Applied to Iris Dataset', fontsize=16)

# 1. Uniform Distribution
# -------------------------------------
# Generate uniform random numbers between min and max of sepal length
min_sepal_length = iris_df['sepal length (cm)'].min()
max_sepal_length = iris_df['sepal length (cm)'].max()

# Generate 100 uniform random numbers between min and max sepal length
uniform_samples = np.random.uniform(min_sepal_length, max_sepal_length, 100)

# Plot original sepal length and uniform distribution
axes[0, 0].hist(iris_df['sepal length (cm)'], bins=10, alpha=0.5, label='Original sepal length')
axes[0, 0].hist(uniform_samples, bins=10, alpha=0.5, color='red', label='Uniform distribution')
axes[0, 0].set_title('Uniform Distribution vs Original Sepal Length')
axes[0, 0].set_xlabel('Sepal Length (cm)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()

# Print explanation
print("\n1. Uniform Distribution:")
print(f"- Min Sepal Length: {min_sepal_length:.2f} cm")
print(f"- Max Sepal Length: {max_sepal_length:.2f} cm")
print("- Generated 100 random samples with equal probability between min and max")
print(f"- Sample mean: {uniform_samples.mean():.2f}")
print(f"- Sample std: {uniform_samples.std():.2f}")

# 2. Normal Distribution
# -------------------------------------
# Calculate mean and standard deviation of petal width
mean_petal_width = iris_df['petal width (cm)'].mean()
std_petal_width = iris_df['petal width (cm)'].std()

# Generate 100 normal random numbers with same mean and std as petal width
normal_samples = np.random.normal(mean_petal_width, std_petal_width, 100)

# Plot original petal width and normal distribution
axes[0, 1].hist(iris_df['petal width (cm)'], bins=10, alpha=0.5, label='Original petal width')
axes[0, 1].hist(normal_samples, bins=10, alpha=0.5, color='green', label='Normal distribution')
axes[0, 1].set_title('Normal Distribution vs Original Petal Width')
axes[0, 1].set_xlabel('Petal Width (cm)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].legend()

# Print explanation
print("\n2. Normal Distribution:")
print(f"- Mean Petal Width: {mean_petal_width:.2f} cm")
print(f"- Std Dev Petal Width: {std_petal_width:.2f} cm")
print("- Generated 100 random samples from normal distribution with same mean and std dev")
print(f"- Sample mean: {normal_samples.mean():.2f}")
print(f"- Sample std: {normal_samples.std():.2f}")

# 3. Poisson Distribution
# -------------------------------------
# Use rounded petal length as lambda for Poisson
# Poisson models count data, so we'll use the average petal length as our lambda
lambda_value = round(iris_df['petal length (cm)'].mean())

# Generate 100 poisson random numbers
poisson_samples = np.random.poisson(lambda_value, 100)

# Plot poisson distribution
axes[1, 0].hist(poisson_samples, bins=range(0, max(poisson_samples) + 2), alpha=0.7, color='purple',
               label=f'Poisson(λ={lambda_value})')
axes[1, 0].set_title(f'Poisson Distribution with λ={lambda_value}')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].legend()

# Print explanation
print("\n3. Poisson Distribution:")
print(f"- Lambda (λ) value: {lambda_value} (rounded mean of petal length)")
print("- Poisson distribution models the number of events in a fixed time/space interval")
print("- Generated 100 random samples from Poisson distribution")
print(f"- Sample mean: {poisson_samples.mean():.2f} (should be close to lambda)")
print(f"- Sample variance: {poisson_samples.var():.2f} (should also be close to lambda)")

# 4. Binomial Distribution
# -------------------------------------
# For binomial, let's use probability of a flower being setosa (1/3 of dataset)
p = len(iris_df[iris_df['species'] == 'setosa']) / len(iris_df)
n = 10  # number of trials

# Generate 100 binomial random numbers
binomial_samples = np.random.binomial(n, p, 100)

# Plot binomial distribution
axes[1, 1].hist(binomial_samples, bins=range(0, n + 2), alpha=0.7, color='orange',
               label=f'Binomial(n={n}, p={p:.2f})')
axes[1, 1].set_title(f'Binomial Distribution with n={n}, p={p:.2f}')
axes[1, 1].set_xlabel('Number of Successes')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].legend()

# Print explanation
print("\n4. Binomial Distribution:")
print(f"- Probability (p) of success: {p:.2f} (proportion of setosa in dataset)")
print(f"- Number of trials (n): {n}")
print("- Binomial distribution models the number of successes in n independent trials")
print("- Generated 100 random samples from Binomial distribution")
print(f"- Sample mean: {binomial_samples.mean():.2f} (should be close to n*p = {n*p:.2f})")
print(f"- Sample variance: {binomial_samples.var():.2f} (should be close to n*p*(1-p) = {n*p*(1-p):.2f})")

# Add more space between subplots
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# Bonus: Creating a distribution comparison for one feature
plt.figure(figsize=(12, 6))
plt.title('Comparing Actual Sepal Width with Different Distributions', fontsize=16)

# Get sepal width data
sepal_width = iris_df['sepal width (cm)']
x = np.linspace(sepal_width.min() - 0.5, sepal_width.max() + 0.5, 1000)

# Plot histogram of actual data
plt.hist(sepal_width, bins=15, density=True, alpha=0.6, label='Actual Sepal Width')

# Fit and plot normal distribution
mu, std = stats.norm.fit(sepal_width)
pdf_norm = stats.norm.pdf(x, mu, std)
plt.plot(x, pdf_norm, 'r-', linewidth=2, label=f'Normal: μ={mu:.2f}, σ={std:.2f}')

# Fit and plot uniform distribution
a, b = sepal_width.min(), sepal_width.max()
pdf_uniform = np.ones_like(x) / (b - a)
pdf_uniform[x < a] = 0
pdf_uniform[x > b] = 0
plt.plot(x, pdf_uniform, 'g-', linewidth=2, label=f'Uniform: [{a:.2f}, {b:.2f}]')

plt.xlabel('Sepal Width (cm)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\nKey Takeaways:")
print("1. Uniform Distribution: Every value between min and max is equally likely.")
print("2. Normal Distribution: Values cluster around the mean with frequency decreasing as you move away.")
print("3. Poisson Distribution: Models count data, good for rare events in fixed intervals.")
print("4. Binomial Distribution: Models number of successes in fixed number of trials.")
print("\nNote: These distributions have different shapes and properties, making them suitable for different types of data.")
