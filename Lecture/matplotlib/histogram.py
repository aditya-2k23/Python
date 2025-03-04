import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.hist(data, bins=10, color='hotpink', edgecolor='white')

plt.title('Basic Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()
