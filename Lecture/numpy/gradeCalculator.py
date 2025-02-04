import numpy as np

a = int(input())

l = list()

for i in range(0, a * 5):
    l.append(list(map(int, input().split())))

x = np.array(l).reshape(a, 5)

print(x)

for i in range(a):
    y = np.mean(x[i])
    print("Average of row ", i, " is: ", y)
