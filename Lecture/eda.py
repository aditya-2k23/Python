import seaborn as sb
import matplotlib.pyplot as plt

iris = sb.load_dataset("iris")

#1. Scatter Plot
sb.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.show()

#2. Histogram

"""
axes[0, 0].hist(data["sepal_length"], bins=30, color="skyblue", edgecolor="black")
axes[0, 0].set_title("Sepal Length")

axes[0, 1].hist(data["sepal_width"], bins=30, color="lightgreen", edgecolor="black")
axes[0, 1].set_title("Sepal Width")

axes[1, 0].hist(data["petal_length"], bins=30, color="salmon", edgecolor="black")
axes[1, 0].set_title("Petal Length")

axes[1, 1].hist(data["petal_width"], bins=30, color="gold", edgecolor="black")
axes[1, 1].set_title("Petal Width")
"""

plt.hist(x=iris["sepal_length"], bins=30, color="skyblue", edgecolor="black")
plt.hist(x=iris["sepal_width"], bins=30, color="lightgreen", edgecolor="black")
plt.hist(x=iris["petal_length"], bins=30, color="salmon", edgecolor="black")
plt.hist(x=iris["petal_width"], bins=30, color="gold", edgecolor="black")
plt.title("Iris Data Histogram")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

#3. Heatmap
corr = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]].corr()
sb.heatmap(data=iris.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#4. Boxplot
sb.boxplot(data=iris, orient="h")
plt.title("Iris Data Boxplot")
plt.show()
