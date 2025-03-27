import pandas as pd

student = [1, 2, 3, 4, 5]
maths = [85, 90, 78, 92, 88]
science = [80, 85, 88, 92, 86]

df = pd.DataFrame({
    "maths": maths,
    "science": science,
})

print(df.mean())
print(df.cov())
print(df.corr())
