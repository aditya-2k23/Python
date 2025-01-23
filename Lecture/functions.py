# ! Basic Functions

def greet():
    print("Welcome to Python Functions!")

def multiply(a, b):
    return a * b

def power(base, exponent = 2):
    return base ** exponent

def sumAll(*nums): # *nums is for? : It is for multiple arguments, it is a tuple
    return sum(nums)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def evenNumbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i # ? yield is user for: It is used to return a list of values, one at a time

def outerFunctions(message):
    def innerFunction():
        print(f"Message from inner function: {message}")
    innerFunction()

    greet()

    print(f"Multiplication of 2 and 3: {multiply(2, 3)}")

    print(f"2 to the power of 3: {power(2, 3)}")

    print(f"Sum of 1, 2, 3, 4, 5: {sumAll(1, 2, 3, 4, 5)}")

    print(f"Factorial of 5: {factorial(5)}")

    print("Even numbers from 0 to 10:")
    print(list(evenNumbers(10)))

outerFunctions("Hello from outer function!")
