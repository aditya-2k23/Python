import numpy as np
import pandas as pd
import seaborn as sb

data = sb.load_dataset('iris')
sepal_width = data["sepal_width"]

mean = np.mean(sepal_width)
df = pd.DataFrame(sepal_width, columns=['Sepal Width'])

std_dev = np.std(sepal_width, ddof=1)
print(f"Mean: {mean:.2f}, Standard Deviation: {std_dev:.2f}")

z_scores = (sepal_width - mean) / std_dev

outliers_z = sepal_width[np.abs(z_scores) > 3]
print(f"Outliers: {len(outliers_z)}")
