import pandas as pd

df = pd.read_csv("./tips.csv")
df["Sum"] = df["Total_Bill"] + df["Tip"]
df["Tip_Percentage"] = ((df["Tip"] / df["Total_Bill"]) * 100).round(2)
df["Tip_Percentage"] = df["Tip_Percentage"].astype(str) + "%"
df["Tip_Percentage"] = df["Tip_Percentage"].replace('nan%', '0%')


print(df.iloc[10:21])

df_filled = df.fillna(0)
print(df_filled.head())

grouped_data = df.groupby('Day')['Total_Bill'].sum()
print(grouped_data)

sorted_df = df.sort_values(by='Total_Bill', ascending=False)
print(sorted_df.head())

df['Total_Bill'] = df['Total_Bill'].apply(lambda x: x / 100)
print(df['Total_Bill'])

pivot_table = df.pivot_table(values="Total_Bill", index="Day", columns="Size", aggfunc='sum')
print(pivot_table)

filtered_df = df.loc[df['Total_Bill'] > 20]
print(filtered_df.head()) # loc is used to access a group of rows and columns by labels or a boolean array.

print("First 5 rows using iloc:\n", df.iloc[0:5]) # iloc is used to get rows (or columns) at particular positions in the index (so it only takes integers).

renamed = df.rename(columns={"Total_Bill": "Total Bill Amount"})
print(renamed.columns)
