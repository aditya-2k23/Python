import pandas as pd

df = pd.read_csv("./tips.csv")
df["Sum"] = df["Total_Bill"] + df["Tip"]
df["Tip_Percentage"] = ((df["Tip"] / df["Total_Bill"]) * 100).round(2)
df["Tip_Percentage"] = df["Tip_Percentage"].astype(str) + "%"
df["Tip_Percentage"] = df["Tip_Percentage"].replace('nan%', '0%')


print(df.iloc[10:21])
