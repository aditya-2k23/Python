import numpy as np

a = np.array([1, 3, 4, 5])
print(a * 2)

a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
d = np.zeros([3, 3], dtype=int)

for i in range(0,len(a)):
    for j in range(0, len(b[0])):
        for k in range(0, len(b)):
            d[i][j] += a[i][k] * b[k][j]

print(a)
print(b)
print(d)
print(a@b)
