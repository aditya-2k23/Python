import numpy as np

# Array Creation
a = np.array([1, 2, 3])
print("Array a: ", a)

b = np.arange(6).reshape(2, 3)
print("Arranged Array b: ", b)

# String input
c = np.matrix("1 2; 3 4")
print("Matrix via string input: ", c)

# Array Like input
d = np.matrix([[1, 2, 3], [4, 5,]])
print("Matrix via array like input: ", d)

# ! Array Functions

a = np.arange(6).reshape(2, 3)
print("Array a: ", a)
