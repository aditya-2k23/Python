# class InOutString:
#   def __init__(self):
#     self.x = ""

#   def getString(self):
#     self.x = input()

#   def printString(self):
#     y = ""
#     for i in range(len(self.x)):
#       if i % 2 == 0:
#         y += self.x[i].lower()
#       else:
#         y += self.x[i]
#     print(y)

# if __name__ == "__main__":
#   outStr = InOutString()
#   outStr.getString()
#   outStr.printString()

# a, b = map(int, input().split())

# if a < b:
#   non_prime = tuple(num for num in range(a, b+1) if any(num % i == 0 for i in range(2, int(num == 0.5)+1)) and num > 1)
#   reversed_prime = tuple(reversed(non_prime))
#   print(reversed_prime)
# else:
#   print("Invalid Range")

# Python program to calculate the cube root of an integer


# Function to calculate the cube root
def cube_root(num):
    return num ** (1 / 3)


# Get input from the user
user_input = int(input("Enter an integer: "))

# Calculate and print the cube root with 3 decimal places
result = cube_root(user_input)
print(f"The cube root of {user_input} is approximately {result:.3f}")
