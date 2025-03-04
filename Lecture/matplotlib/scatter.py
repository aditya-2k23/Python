import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', linestyle='-', color='g', label='Lines')
plt.scatter(x, y, color='r', marker='o', s=100, label='Points')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Diagram')

plt.legend() # Legend is used to show the labels of the plot
plt.show()
