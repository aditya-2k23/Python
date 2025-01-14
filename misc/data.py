import matplotlib.pyplot as plt
import pandas as pd

# Data from the image
data = {
    "Name": ["Aditya", "Sukhpreet", "Sakshi", "Dev", "Simran"],
    "Reg.No": [12308561, 12456789, 12306871, 12356782, 12308910],
    "Roll No": [49, 53, 51, 52, 50],
    "Section": ["K23SM", "K23TO", "K23SM", "K23TO", "K23TO"],
    "Age": [19, 19, 20, 20, 21]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Group by Age and count students in each age group
age_distribution = df.groupby("Age")["Name"].count()

# Plotting the bar graph
plt.figure(figsize=(8, 5))
age_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Student Age Distribution", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot to a file
plt.savefig("./student_age_distribution.png")
plt.show()
