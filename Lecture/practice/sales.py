from colorama import Fore
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("sales.xlsx")

print(Fore.RED + "Shape of data:", Fore.RESET, end=" ")
print(data.shape, "\n")

print(Fore.CYAN + "Columns of data:", Fore.RESET)
print(data.columns.tolist(), "\n")

print(Fore.MAGENTA + "Info of data:", Fore.RESET)
print(data.info(), "\n")

print(Fore.GREEN + "Head of data:", Fore.RESET)
print(data.head(), "\n")

print(Fore.YELLOW + "Describe data:", Fore.RESET)
print(data.describe(), "\n")

print(Fore.BLUE + "Checking Missing Values:", Fore.RESET)
print(data.isnull().sum(), "\n")

# Sales date & Sales quantity Correlation
df = pd.DataFrame({
    "Sales_date": data["SalesDate"],
    "Sales_quantity": data["Sales_Qty"]
})

print(Fore.LIGHTRED_EX + "Sales Date & Sales Quantity Correlation:" + Fore.RESET, end=" ")
print(f"{df.corr().iloc[0, 1]:.2f}")
print(Fore.LIGHTYELLOW_EX + "Sales Date & Sales Quantity Covariance:" + Fore.RESET, end=" ")
print(f"{df.cov().iloc[0, 1]:.2f}")

df = pd.DataFrame({
    "Sales Cost": data["Sales_Cost"],
    "Sales Amount": data["Sales_Amt"]
})

# Sales Cost & Sales Amount
print(Fore.LIGHTRED_EX + "Sales Cost & Sales Amount Correlation:" + Fore.RESET, end=" ")
print(f"{df.corr().iloc[0, 1]:.2f}")
print(Fore.LIGHTYELLOW_EX + "Sales Cost & Sales Amount Covariance:" + Fore.RESET, end=" ")
print(f"{df.cov().iloc[0, 1]:.2f}")


df = pd.DataFrame({
    "Sales Cost": data["Sales_Cost"],
    "Sales Amount": data["Sales_Amt"],
})

# Histogram
plt.hist(x=df, bins=15)
plt.title("Histogram")
plt.xlabel("Sales Cost")
plt.ylabel("Sales Amount")
plt.show()
