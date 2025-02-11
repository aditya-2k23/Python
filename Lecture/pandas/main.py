import pandas as pd

a = pd.Series([1, 2, 3])
print(a)

b = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
print(b)

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)

data = {'a': 0.0, 'b': 1.0, 'c': 2.0}
s = pd.Series(data, index=['b', 'c', 'a'])
print(s)

list = ['g', 'e', 'e', 'k', 's']
s = pd.Series(list)
print(s)

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
l = ['c', 'e']
print("b   ", s['b'])
print("e   ", s['e'])
print(s[l])
print(s[['a', 'e']])

print("Location of b")
print(s.loc['b'])

print("Index location of b")
print(s.iloc[1])

### ! DataFrame

c = pd.DataFrame(b)
print(c)

d = pd.DataFrame(c, columns=["Roll No"])
print(d)

d1 = pd.DataFrame(b, columns=["Roll No"])
print(d1)


### ! Dataframe from list
d = {"one": pd.Series([1, 2, 3], index=['a', 'b', 'c']), "two": pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df[2:4])

### ! Addition of rows
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df._append(df2)
print(df)

### ! Deletion of rows
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df._append(df2)

df = df.drop(0)
print(df)
