while True:
    first = int(input("Enter your first number: "))
    operator = input("Enter operator (+,-,*,/,%): ")
    second = int(input("Enter your second number: "))

    if operator == "+":
        print(first + second)
    elif operator == "-":
        print(first - second)
    elif operator == "*":
        print(first * second)
    elif operator == "/":
        print(first / second)
    elif operator == "%":
        print(first % second)
    else:
        print("Invalid Operation")

    choice = input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != "yes":
        break
