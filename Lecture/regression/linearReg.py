import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create or load the DataFrame
# Example data
data = {
    'Advertising Budget': [1, 2, 3, 4, 5],  # in $1000s
    'Sales': [1.5, 2.0, 2.5, 3.5, 4.0]      # in $1000s
}

df = pd.DataFrame(data)

# Step 2: Separate features (X) and target (y)
x = df[['Advertising Budget']]  # 2D array for sklearn
y = df['Sales']                 # 1D array

# Step 3: Perform linear regression
model = LinearRegression()
model.fit(x, y)

# Step 4: Get slope and intercept
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope (m): {slope}")
print(f"Intercept (c): {intercept}")

# Step 5: Predict sales using the regression line
df['Predicted Sales'] = model.predict(x)

# Step 6: Correlation coefficient using NumPy
correlation_matrix = np.corrcoef(df['Advertising Budget'], df['Sales'])
correlation = correlation_matrix[0, 1]
print(f"Correlation Coefficient (r): {correlation:.2f}")

# Step 7: Visualization
plt.figure(figsize=(8, 5))
plt.scatter(df['Advertising Budget'], df['Sales'], color='blue', label='Actual Sales')
plt.plot(df['Advertising Budget'], df['Predicted Sales'], color='red', label='Regression Line')

plt.title("Advertising Budget vs Sales")
plt.xlabel("Advertising Budget ($1000s)")
plt.ylabel("Sales ($1000s)")
plt.grid(True)
plt.legend()
plt.show()
