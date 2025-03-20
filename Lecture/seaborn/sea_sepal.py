import seaborn as sb
import matplotlib.pyplot as plt

iris = sb.load_dataset("iris")

#1. Scatter Plot - Sepal Length vs Sepal Width
plt.figure(figsize=(7, 5))
sb.scatterplot(x="sepal_length", y="sepal_width", hue="species", style="species", data=iris, palette="deep")
plt.title("Scatter Plot of Sepal Length vs Sepal Width")
plt.show()

#2. Line Plot - Sepal Length vs Petal Length by Species
plt.figure(figsize=(7, 5))
sb.lineplot(x="sepal_length", y="petal_length", hue="species", marker="o", data=iris, palette="tab10")
plt.title("Line Plot of Sepal Length vs Petal Length by Species")
plt.show()
