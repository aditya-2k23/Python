import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sb
import statsmodels.api as sm

df = sb.load_dataset("iris")

print("Sepal Length")
sample = df["sepal_length"].sample(30, random_state=42)
pop_mean = df['sepal_length'].mean()
pop_std = df["sepal_length"].std()
z_score = (sample.mean() - pop_mean) / (pop_std / np.sqrt(len(sample)))
p_value = stats.norm.sf(abs(z_score)) * 2
print(f"Z-test: Z-score = {z_score:.4f}, p-value = {p_value:.4f}")

print("Sepal Width")
sample = df["sepal_width"].sample(30, random_state=42)
pop_mean = df['sepal_width'].mean()
pop_std = df["sepal_width"].std()
z_score = (sample.mean() - pop_mean) / (pop_std / np.sqrt(len(sample)))
p_value = stats.norm.sf(abs(z_score)) * 2
print(f"Z-test: Z-score = {z_score:.4f}, p-value = {p_value:.4f}")

print("Petal Length")
sample = df["petal_length"].sample(30, random_state=42)
pop_mean = df['petal_length'].mean()
pop_std = df["petal_length"].std()
z_score = (sample.mean() - pop_mean) / (pop_std / np.sqrt(len(sample)))
p_value = stats.norm.sf(abs(z_score)) * 2
print(f"Z-test: Z-score = {z_score:.4f}, p-value = {p_value:.4f}")

print("Petal Width")
sample = df["petal_width"].sample(30, random_state=42)
pop_mean = df['petal_width'].mean()
pop_std = df["petal_width"].std()
z_score = (sample.mean() - pop_mean) / (pop_std / np.sqrt(len(sample)))
p_value = stats.norm.sf(abs(z_score)) * 2
print(f"Z-test: Z-score = {z_score:.4f}, p-value = {p_value:.4f}")
