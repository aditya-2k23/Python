from colorama import Fore, Style

import pandas as pd
import seaborn as sb

data = sb.load_dataset("Iris")

df = pd.DataFrame({
    "Sepal_length": data["sepal_length"],
    "Sepal_width": data["sepal_width"],
})

df2 = pd.DataFrame({
    "Petal_length": data["petal_length"],
    "Petal_width": data["petal_width"]
})

print(Fore.GREEN + "Sepal Length vs Sepal Width")
print(Fore.LIGHTBLUE_EX + "Covariance:", end=" ")
print(Fore.WHITE, f"{df.cov().iloc[0, 1]:.2f}")
print(Fore.YELLOW + "Correlation:", end=" ")
print(Fore.WHITE, f"{df.corr().iloc[0, 1]:.2f}")

print(Fore.CYAN + "\nPetal Length vs Petal Width")
print(Fore.LIGHTBLUE_EX + "Covariance:", end=" ")
print(Fore.WHITE, f"{df2.cov().iloc[0, 1]:.2f}")
print(Fore.YELLOW + "Correlation:", end=" ")
print(Fore.WHITE, f"{df2.corr().iloc[0, 1]:.2f}", Fore.RESET)
