import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from scipy import stats

# ! Q1
df = pd.DataFrame({
    'Restaurant Name': [
        'Bella Vita', 'Spice Garden', 'The Olive Branch', 'Taco Fiesta',
        'Sushi Haven', 'Pasta Palazzo', 'Curry Corner', 'La Burrito',
        'Dragon Wok', 'Mediterranean Breeze'
    ],
    'Rating': [4.8, 4.2, 4.6, 4.0, 4.9, 4.3, 4.7, 3.9, 4.5, 4.8],
    'Number of Reviews': [150, 80, 200, 50, 120, 90, 180, 30, 110, 160],
    'Cuisine': [
        'Italian', 'Indian', 'Mediterranean', 'Mexican',
        'Japanese', 'Italian', 'Indian', 'Mexican',
        'Chinese', 'Mediterranean'
    ]
})
# Find the restaurant with the highest number of reviews
print(df.loc[df["Number of Reviews"].idxmax(), "Restaurant Name"])

# Average rating by cuisine
avg_rating = df.groupby("Cuisine")["Rating"].mean()
print(avg_rating)

# Bar plot
# plt.figure(figsize=(10, 6))
# plt.bar(avg_rating.index, avg_rating.values)
# plt.title("Average Rating for each cuisine")
# plt.xlabel("Cuisine")
# plt.ylabel("Rating")
# plt.show()

# Total Reviews for each cuisine
total_reviews = df.groupby("Cuisine")["Number of Reviews"].sum()
print(total_reviews)

# Pie Chart
# plt.pie(total_reviews, labels=total_reviews.index)
# plt.title("Distribution of Reviews by Cuisine")
# plt.show()

# Top rated restaurants
top_rated = df[(df["Rating"] > 4.5) & (df["Number of Reviews"] > 100)]
print("Top Rated Restaurants:")
print(top_rated[["Restaurant Name", "Rating"]])

# Hist Plot
# plt.hist(top_rated["Rating"], bins=5, color="lightgreen", edgecolor='black')
# plt.title("Top Rated Restaurants")
# plt.xlabel("Rating")
# plt.ylabel("Number of Restaurants")
# plt.xticks([4.5, 4.6, 4.7, 4.8, 4.9])
# plt.yticks(range(0, 3))
# plt.show()

# ! Q2
df2 = pd.DataFrame({
    'Car Model': [
        'Toyota Camry', 'Honda Civic', 'Ford Mustang', 'Chevrolet Malibu',
        'Hyundai Sonata', 'Toyota Corolla', 'Honda Accord', 'Nissan Altima',
        'BMW 3 Series', 'Volkswagen Jetta'
    ],
    'Year': [2018, 2019, 2020, 2017, 2019, 2021, 2018, 2020, 2019, 2017],
    'Price': [18000, 15000, 25000, 17000, 16000, 19000, 20000, 14000, 28000, 13000],
    'Mileage': [45000, 30000, 20000, 60000, 35000, 15000, 40000, 50000, 25000, 70000]
})

# Average price for each car model
avg_price = df2.groupby("Car Model")["Price"].mean()
print(avg_price)

# Find the car with the lowest mileage
lowest_mileage = df2.loc[df2["Mileage"].idxmin(), "Car Model"]
print("Car Model with the lowest mileage:", end=" ")
print(lowest_mileage)

# Bar plot
# plt.figure(figsize=(14, 7))
# plt.bar(avg_price.index, avg_price.values, color="coral", edgecolor='black')
# plt.title("Average Price for each Car Model")
# plt.xlabel("Car Model")
# plt.ylabel("Price ($)")
# plt.yticks(range(0, 30001, 5000))
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# Hist Plot
# plt.figure(figsize=(8, 5))
# plt.hist(df2["Mileage"], bins=5, color="lightblue", edgecolor='black')
# plt.title("Mileage distribution")
# plt.xlabel("Mileage")
# plt.ylabel("Number of Cars")
# plt.yticks(range(0, 5))
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

# Good Value Cars for money
good_value_cars = df2[(df2["Price"] < 20000) & (df2['Mileage'] < 50000)]
print(good_value_cars[["Car Model", "Price", "Mileage"]])

# ! Q3
df3 = pd.DataFrame({
    'Course ID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010'],
    'Course Name': [
        'Python Programming', 'Data Science Basics', 'Web Development', 'Machine Learning',
        'Java Programming', 'SQL for Beginners', 'AI Fundamentals', 'Cloud Computing',
        'Cybersecurity Essentials', 'Digital Marketing'
    ],
    'Enrollment Count': [1500, 800, 2000, 1200, 900, 1800, 600, 1100, 1400, 700],
    'Average Rating': [4.7, 4.3, 4.8, 4.6, 4.2, 4.9, 4.1, 4.5, 4.4, 4.0]
})

# Total Enrollment
total_enrollment = df3.groupby("Course Name")["Enrollment Count"].sum()
print(total_enrollment)

# Highest Average Rating
highest_avg_rating = df3.loc[df3["Average Rating"].idxmax(), "Course Name"]
print("Course with the highest average rating:", highest_avg_rating)

print("Average Enrollment Count:", np.mean(df3["Enrollment Count"]))
print("Median:", np.median(df3["Enrollment Count"]))
print(f"Standard Deviation: {np.std(df3["Enrollment Count"]):.2f}")

# Hist plot
# sb.histplot(data=total_enrollment, bins=5, color="coral")
# plt.title("Distribution of Enrollment Count")
# plt.xlabel("Course Name")
# plt.ylabel("Enrollment Count")
# plt.yticks(range(0, 5))
# plt.show()

# Box plot
# plt.figure(figsize=(10, 6))
# sb.boxplot(x="Course Name", y="Average Rating", data=df3)
# plt.title('Average Rating by Course')
# plt.xticks(rotation=45)
# plt.xlabel('Course Name')
# plt.ylabel('Average Rating')
# plt.tight_layout()
# plt.show()

# Popular courses
popular_courses = df3[(df3["Enrollment Count"] > 1000) & (df3['Average Rating'] > 4.5)]
print(popular_courses[["Course Name"]])

# Scatter plot
# plt.figure(figsize=(10,6))
# sb.scatterplot(x="Enrollment Count", y="Average Rating", data=df3, color="blue", label="All Courses")
# sb.scatterplot(x="Enrollment Count", y="Average Rating", data=popular_courses, color="red", label="Popular Courses")
# plt.axhline(y=4.5, color='green', linestyle='--', label='Rating = 4.5')
# plt.axvline(x=1000, color='purple', linestyle='--', label='Enrollment = 1000')
# plt.title('Enrollment Count vs Average Rating')
# plt.xlabel('Enrollment Count')
# plt.ylabel('Average Rating')
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# ! Q4 (Linear Regression)
df4 = pd.DataFrame({
    'Advertising Budget': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Sales': [15, 25, 35, 45, 50, 55, 65, 70, 80, 85]
})

# x = df4[["Advertising Budget"]]
# y = df4["Sales"]

# model = LinearRegression()
# model.fit(x, y)

# slope = model.coef_[0]
# intercept = model.intercept_
# print(f"Slope: {slope:.2f}")
# print(f"Intercept: {intercept:.2f}")

# correlation = np.corrcoef(df4["Advertising Budget"], df4["Sales"])[1, 0]
# print(f"Correlation Coefficient: {correlation:.2f}")

# Scatter Plot
# plt.figure(figsize=(10,6))
# plt.scatter(df4["Advertising Budget"], df4["Sales"], color="blue", label="Data Points")
# plt.plot(df4["Advertising Budget"], model.predict(x), color="red", label="Regression Line")
# plt.title('Sales vs Advertising Budget')
# plt.xlabel('Advertising Budget ($1000)')
# plt.ylabel('Sales ($1000)')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.tight_layout()
# plt.show()

# budget = np.array([[50]])
# predicted_sales = model.predict(budget)[0]
# print(f"\nPredicted Sales for $50,000 Advertising Budget: ${predicted_sales*1000:.2f}")

# residuals = y - model.predict(x)
# plt.figure(figsize=(10, 6))
# sb.scatterplot(x=model.predict(x), y=residuals, color="purple")
# plt.axhline(y=0, color="black", linestyle="--")
# plt.title('Residual Plot for Linear Regression')
# plt.xlabel('Predicted Sales ($1000)')
# plt.ylabel('Residuals')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# R-squared value
# r_squared = r2_score(y, model.predict(x))
# print(f"R-squared Value: {r_squared:.2f}")

# ! Q5
df5 = pd.DataFrame({
    'Square Footage': [1200, 1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500],
    'Price': [150, 180, 210, 240, 260, 290, 310, 340, 360, 400]
})

x = df5[["Square Footage"]]
y = df5["Price"]

model = LinearRegression()
model.fit(x, y)

slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope: {slope:.4f}, Intercept: {intercept:.4f}")

print(f"Square Footage Mean: {np.mean(df5["Square Footage"])}, Standard variance: {np.std(df5["Square Footage"]):.4f}")
print(f"Square Footage Mean: {np.mean(df5["Price"])}, Standard variance: {np.std(df5["Price"]):.4f}")

# Scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(df5["Square Footage"], df5["Price"], color="red", label="Data Points")
# plt.plot(df5["Square Footage"], model.predict(x), color="blue", label="Regression Line")
# plt.title("Data Points and the Regression Line")
# plt.xlabel("Square Footage")
# plt.ylabel("Price")
# plt.legend()
# plt.grid(True, alpha=0.7, linestyle="--")
# plt.show()

price = np.array([[2000]])
predicted_price = model.predict(price)[0]
print(f"\nPredicted Price for 2000 Square Feet: ${predicted_price*1000:.2f}")

# Scatter plot
# plt.figure(figsize=(10,6))
# sb.regplot(x="Square Footage", y="Price", data=df5, scatter_kws={"color": "blue"}, line_kws={"color":"red"})
# plt.title('Price vs Square Footage with Regression Line')
# plt.xlabel('Square Footage')
# plt.ylabel('Price ($1000)')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# Mean Squared Error (MSE)
mse = mean_squared_error(y, model.predict(x))
print(f"Mean Squared Error (MSE): {mse:.2f}")

# ! Q6
df6 = pd.DataFrame({
    'Student ID': ['S001', 'S002', 'S003 Rouse', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010'],
    'Math Score': [85, 92, 78, 65, 95, 88, 72, 90, 60, 98],
    'Science Score': [80, 90, 75, 70, 92, 85, 68, 88, 65, 95],
    'English Score': [82, 88, 80, 68, 90, 84, 70, 85, 62, 93]
})

stats = df6[["Math Score", "Science Score", "English Score"]].agg(["mean", "median", "std"]).round(2)
print(stats)

correlation_matrix = np.corrcoef(df6[["Math Score", "Science Score", "English Score"]].values.T)
print("\nCorrelation Matrix")
print(pd.DataFrame(correlation_matrix, columns=["Math", "Science", "English"], index=["Math", "Science", "English"]))
# print(df6[["Math Score", "Science Score", "English Score"]].corr())

# Heatmap
# plt.figure(figsize=(8, 6))
# sb.heatmap(correlation_matrix, annot=True, cmap="coolwarm", xticklabels=['Math', 'Science', 'English'], yticklabels=['Math', 'Science', 'English'])
# plt.title("Correlation between the subject marks")
# plt.tight_layout()
# plt.show()

# Detect outliers in Math Scores using IQR
Q1 = df6["Math Score"].quantile(0.25)
Q3 = df6["Math Score"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df6[(df6["Math Score"] < lower) | (df6["Math Score"] > upper)]["Math Score"]
print("\nOutliers in Math Score")
print(outliers.tolist() if not outliers.empty else "No outliers detected")

# Above 90 percentile
percentile_90 = df6[["Math Score", "Science Score", "English Score"]].quantile(0.9)
high_performers = df6[
    (df6["Math Score"] > percentile_90["Math Score"]) &
    (df6["Science Score"] > percentile_90["Science Score"]) &
    (df6["English Score"] > percentile_90["English Score"])
]
print("\nStudents above 90th percentile in all subjects:")
print(high_performers[['Student ID', 'Math Score', 'Science Score', 'English Score']])

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
subjects = ["Math Score", "Science Score", "English Score"]
colors = ["skyblue", "lightgreen", "salmon"]
for i, subject in enumerate(subjects):
    axes[i].hist(df6[subject], bins=5, color=colors[i], edgecolor='black')
    axes[i].set_title(f"{subject} Distribution")
    axes[i].set_xlabel(subject)
    axes[i].set_ylabel("Number of Students")
    axes[i].grid(axis='y', linestyle='--', alpha=0.75)
plt.tight_layout()
plt.show()

# Shapiro-Wilk test for Math Score normality
stat, p_value = stats.shapiro(df6["Math Score"])
print(f"\nShapiro-Wilk test statistic: {stat:.4f}, p-value: {p_value:.4f}")

if p_value > 0.05:
    print("Math Score distribution is normal (fail to reject H0)")
else:
    print("Math Score distribution is not normal (reject H0)")
