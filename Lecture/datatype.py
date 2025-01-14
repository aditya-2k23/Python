
from colorama import Fore, Style, init

# Initialize colorama
init()

# Different data types in Python.
print(f"{Fore.YELLOW}Data Types{Style.RESET_ALL}")

# Integer
age = 25
print(f"{Fore.RED}Age: {age}, Type: {type(age)}{Style.RESET_ALL}")

# Float
height = 5.9
print(f"{Fore.GREEN}Height: {height}, Type: {type(height)}{Style.RESET_ALL}")

# String
name = "Alice"
print(f"{Fore.BLUE}Name: {name}, Type: {type(name)}{Style.RESET_ALL}")

# Boolean
is_student = True
print(f"{Fore.YELLOW}Is Student: {is_student}, Type: {type(is_student)}{Style.RESET_ALL}")

# List
fruits = ["Apple", "Banana", "Cherry"]
print(f"{Fore.CYAN}Fruits: {fruits}, Type: {type(fruits)}{Style.RESET_ALL}")

# Tuple
coordinates = (10.5, 20.5)
print(f"{Fore.MAGENTA}Coordinates: {coordinates}, Type: {type(coordinates)}{Style.RESET_ALL}")

# Set
unique_numbers = {1, 2, 3, 4, 5}
print(f"{Fore.WHITE}Unique Numbers: {unique_numbers}, Type: {type(unique_numbers)}{Style.RESET_ALL}")

# Dictionary
person = {"name": "Alice", "age": 25, "is_student": True}
print(f"{Fore.LIGHTBLUE_EX}Person: {person}, Type: {type(is_student)}{Style.RESET_ALL}")

# Demonstrating type conversion
print("\n")
print(f"{Fore.YELLOW}Type Conversion{Style.RESET_ALL}")

# Integer to String
age_str = str(age)
print(f"{Fore.RED}Age (String): {age_str}, Type: {type(age_str)}{Style.RESET_ALL}")

# String to Float
height_str = "5.9"
height_float = float(height_str)
print(f"{Fore.GREEN}Height (Float): {height_float}, Type: {type(height_float)}{Style.RESET_ALL}")

# List to Set
unique_fruits = set(fruits)
print(f"{Fore.CYAN}Unique Fruits: {unique_fruits}, Type: {type(unique_fruits)}{Style.RESET_ALL}")
