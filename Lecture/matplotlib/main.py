import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

colors = mcolors.CSS4_COLORS
print(list(colors.keys()))
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# plt.plot(x, y, marker='o', linestyle='-' ,color='r', label='Line 1')

# '''
# marker:
# 'o'     Circle
# '^'     Triangle (Up)
# 'v'     Triangle (Down)
# 's'     Square
# 'D'     Diamond
# 'x'     Cross
# '+'     Plus Sign
# 'p'     Pentagon
# 'h'     Hexagon
# '.'     Small Dot
# '''

# plt.xlabel('x-axis label')
# plt.ylabel('y-axis label')
# plt.title('Basic Line Plot')

# plt.legend()

# plt.show()

categories = ["AB", 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values, color='yellow')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Chart')

plt.show()
