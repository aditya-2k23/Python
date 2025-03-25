import seaborn as sb
import matplotlib.pyplot as plt

iris = sb.load_dataset("iris")

#1. Scatter Plot
sb.scatterplot(iris, x="sepal_length", y="sepal_width", hue="species")
plt.show()

#2. Histogram
sb.histplot(iris["sepal_length"], bins=30, color="skyblue", edgecolor="black")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

#3. Heatmap
corr = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]].corr()
sb.heatmap(corr, annot=True)
plt.show()
