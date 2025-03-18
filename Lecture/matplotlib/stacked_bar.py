import numpy as np
import matplotlib.pyplot as plt

categories = ["Category A", "Category B", "Category C", "Category D"]
values1 = [4, 7, 1, 8]
values2 = [6, 2, 4, 5]
values3 = [5, 3, 2, 4]

x = np.arange(len(categories))

fig, ax = plt.subplots()
ax.bar(x, values1, label="Group 1" , color="#ff9999")
ax.bar(x, values2, bottom=values1, label="Group 2", color="#66b3ff")
ax.bar(x, values3, bottom=np.array(values1) + np.array(values2), label="Group 3", color="#99ff99")

ax.set_xlabel("Categories")
ax.set_ylabel("Values")
ax.set_title("Stacked Bar Chart Example")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.show()
