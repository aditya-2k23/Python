import numpy as np

data = np.array([10, 12, 14, 15, 18, 21, 22, 25, 28, 30, 2, -10])

mean = np.mean(data)
std_dev = np.std(data)
print(f"Mean: {mean:.2f}, Standard Deviation: {std_dev:.2f}")
z_scores = (data - mean) / std_dev
for i, z in enumerate(z_scores):
    print(f"Z_{i + 1} = {z:.2f}")
