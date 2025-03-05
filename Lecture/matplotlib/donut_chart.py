import matplotlib.pyplot as plt

sizes = [30, 20, 25, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen', 'violet']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors,  autopct="%1.1f%%", startangle=90)

center_circle = plt.Circle((0, 0), 0.6, fc='white')
'''
(x, y) -> The coordinates of the circle's center.
radius -> The radius of the circle.
'''
ax.add_artist(center_circle)

ax.set_aspect('equal')
'''
'equal' -> Ensures that one unit on the x-axis is the same length as one unit
'auto' -> The aspect ratio is adjusted automatically based no the axis limits.
'''

plt.title("Donut Chart Example")
plt.show()
