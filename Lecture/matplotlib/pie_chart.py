import matplotlib.pyplot as plt

labels = ["Apple", "Banana", "Cherry", "Dates"]
sizes = [30, 20, 40, 10]

plt.pie(sizes, labels=labels, autopct='%1.2f%%')
# autopct is used to display the percentage of each slice

plt.title('Pie Chart')

plt.show()
