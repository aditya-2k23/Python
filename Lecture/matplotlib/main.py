import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', linestyle='-' ,color='r', label='Line 1')

'''
marker:
'o'     Circle
'^'     Triangle (Up)
'v'     Triangle (Down)
's'     Square
'D'     Diamond
'x'     Cross
'+'     Plus Sign
'p'     Pentagon
'h'     Hexagon
'.'     Small Dot
'''

plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('Basic Line Plot')

plt.legend()

plt.show()
