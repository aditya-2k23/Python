import pandas as pd
import numpy as np

l = [12, 25, 56, 88]
df = pd.DataFrame(l, columns=['RollNo'])
print(df)

data = np.array([90, 75, 50, 66])
s = pd.Series(data)
print(s)

data = np.array(['a', 'b', 'c', 'd'])



data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)

data = {"Ahmed": 92, "Ali": 55, "Omar": 83}
s = pd.Series(data, index=["Ali", "Ahmed", "Omar"])
print(s)
