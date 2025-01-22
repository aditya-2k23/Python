# Break Statement
print("Break Example")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i = 5")
        break
    print(i)

# Continue Statement
print("\nContinue Example")
for i in range(10):
    if i == 5:
        print("Skipping i = 5")
        continue
    print(i)

# Pass Statement
print("\nPass Example")
for i in range(10):
    if i == 5:
        print("Skipping i = 5")
        pass
    print(i)

# Nested Loops
print("\nNested Loops Example")
for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")

# Match-Case Statement
print("\nMatch-Case Example")
status_code = int(input("Enter a status code: "))
match status_code:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")
