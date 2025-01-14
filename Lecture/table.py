from colorama import Fore, Style, init

init()

# 10 Colors
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]

num = int(input())
print("Multiplication Table of", num)
for i in range(1, 11):
    print(f"{colors[i % 10]}{num} x {i} = {num * i}{Style.RESET_ALL}")
