from scipy.stats import uniform, binom, poisson
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

### Uniform
mean = 100
a, b, x1, x2 = 0, 30, 0, 10
prob = uniform.cdf(x2, loc=a, scale=b-a) - uniform.cdf(x1, loc=a, scale=b-a)
print(f"Probability of uniform distribution between {x1} and {x2}: {prob:.4f}")

### Normal
sd = 5
size = 100000
data = np.random.normal(mean, sd, size)
sb.histplot(data, kde=True)
plt.show()

### Binomial
n = 10
p = 0.5
k = 6
prob = binom.pmf(k, n, p)
print(f"Probability of getting {k} successes in {n} trials: {prob:.4f}")

### Poisson
a = 3
k = 5
prob = poisson.pmf(k, mu=a)
print(f"P(x = {k}): {prob:.4f}")
