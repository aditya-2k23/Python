import numpy as np

# Taking input for the first array
a = np.array(list(map(int, input("Enter the elements of the first array separated by space: ").split())))
print(a * 2)

# Taking input for the matrices
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

print("Enter the elements of the first matrix row-wise:")
a = np.array([list(map(int, input().split())) for _ in range(rows)])

print("Enter the elements of the second matrix row-wise:")
b = np.array([list(map(int, input().split())) for _ in range(rows)])

d = np.zeros([rows, cols], dtype=int)

for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            d[i][j] += a[i][k] * b[k][j]

print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Matrix D (Result of A * B):")
print(d)
print("Matrix A @ B (Using @ operator):")
print(a @ b)
