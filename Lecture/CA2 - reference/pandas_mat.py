import pandas as pd
import matplotlib.pyplot as plt
#Load dataset

df = pd.read_csv("./sample_superstore.csv")
#Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y')
#1. Sales Trends Over Time
#How do total sales vary over different months and years?
df['Year-Month'] = df['Order Date'].dt.to_period('M')
'''
  Parameter	Description	Example Output
  'Y'	Yearly	2023
  'M'	Monthly	2023-01
  'Q'	Quarterly	2023Q1
  'W'	Weekly	2023-05-14 (Week starting)
  'D'	Daily	2023-05-14
  'H'	Hourly	2023-05-14 15:00
  'T' or 'min'	Minute	2023-05-14 15:30
'''
sales_trend = df.groupby('Year-Month')['Sales'].sum()
plt.figure(figsize=(12, 6))
sales_trend.plot(marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

#2. Most Profitable Categories
#Which product categories generate the highest profit?
plt.figure(figsize=(8, 5))
category_profit = df.groupby('Category')['Profit'].sum().sort_values()
category_profit.plot(kind='bar', color='skyblue')
plt.title('Total Profit by Category')
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.show()

# 3. Regional Performance
#Which regions contribute the most to sales and profit?
plt.figure(figsize=(10, 5))
region_sales = df.groupby('Region')['Sales'].sum().sort_values()
region_sales.plot(kind='bar', color='lightcoral')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

# 4. Customer Segments Analysis
#How do different customer segments (Consumer, Home Office, Corporate) contribute to sales and profit?
plt.figure(figsize=(6, 6))
df['Segment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Distribution by Customer Segment')
plt.ylabel('')
plt.show()

#5. Impact of Discounts on Profitability
#How does increasing the discount percentage affect profitability?
plt.figure(figsize=(8, 5))
plt.scatter(df.Discount,df.Profit,color="blue",marker='o')
plt.title('Impact of Discount on Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.show()

# 6. Best and Worst Performing States
#Which states have the highest and lowest total sales?
plt.figure(figsize=(12, 6))
state_sales = df.groupby('State/Province')['Sales'].sum().sort_values()
state_sales[-10:].plot(kind='barh', color='seagreen')
plt.title('Top 10 States by Sales')
plt.xlabel('Total Sales')
plt.ylabel('State')
plt.show()

# 7. Top Selling Products
#What are the top 10 most sold products in terms of quantity?
top_products = df.groupby('Product Name')['Quantity'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='orange')
plt.title('Top 10 Selling Products by Quantity')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45, ha='right')
plt.show()

# 8. Shipping Mode Preferences
#What are the most commonly used shipping modes, and how do they impact sales and delivery time?
plt.figure(figsize=(8, 5))
df['Ship Mode'].value_counts().plot(kind='bar', color='purple')
plt.title('Shipping Mode Preferences')
plt.xlabel('Shipping Mode')
plt.ylabel('Number of Orders')
plt.show()

# 9. Order Frequency by Customer
#How many customers place multiple orders, and what percentage of orders come from repeat customers?
customer_orders = df.groupby('Customer Name')['Order ID'].nunique()
plt.figure(figsize=(8, 5))
customer_orders.hist(bins=20, color='teal', edgecolor='black')
plt.title('Order Frequency by Customer')
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.show()

# 10. Seasonality in Sales
#Are there certain months where sales peak, indicating seasonality?
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].mean()
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind='bar', color='darkblue')
plt.title('Average Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.xticks(rotation=0)
plt.show()
