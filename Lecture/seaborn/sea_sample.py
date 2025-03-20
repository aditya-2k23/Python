import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

file_path = "./sample_superstore.xls"
data = pd.read_excel(file_path, sheet_name='samplesuperstore')

#Preview the data
print(data.head())
#Set Style
sns.set(style="whitegrid")

#1. Line Plot - Sales over Order Data
plt.figure(figsize=(10,5))
data['Order Date'] = pd.to_datetime(data['Order Date'])
sns.lineplot(data=data, x='Order Date',y='Sales')
plt.title('Sales Trend Over Time')
# plt.show()

#2. Bar Plot - Average Profit by Category
plt.figure(figsize=(8,5))
barplot = sns.barplot(x=data["Category"],y=data["Profit"],errorbar=None)
for p in barplot.patches:
    value = f'{p.get_height():.2f}' #2 decimal Places
    barplot.annotate(value,
                     (p.get_x()+ p.get_width()/2., p.get_height()),
                     he='center', va='center', fontsize=10, color='black',
                     xytext=(0,5), textcoords='offset points')

plt.title('Average profit by category')
plt.show()
