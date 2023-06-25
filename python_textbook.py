# print("Save Earth")
# print("Preserve Future")

# gender = "M"
# message = "Keep Smiling"
# price = 987.9

# To display values of variables
# message = "Keep Smiling"
# print(message)
# userNo = 101
# print("User Number is", userNo)

# To find the area of a rectangle
# length = 10
# breadth = 20
# area = length * breadth

# print(area)

# num1 = 10
# num2 = 20
# result = num1 + num2
# print(result)

# a = [1, 2, 3]
# print(2 in a)

# print("I", "Love", "My", "Country")

# Explicit type conversion from int to float
# num1 = 10
# num2 = 20
# num3 = num1 + num2
# print(num3)
# num4 = float(num1 + num2)
# print(num4)

# Total_Marks = 10
# print(Total_Marks)

# first = "Mohandas "
# second = "Karamchand "
# last = "Gandhi"
# full_name = first + second + last
# print(full_name)

# num1 = 20
# num2 = -10
# num3 = num1 + num2


# def test():
#     check1 = num3 < 12
#     check2 = num3 > 24
#     print(check1)
#     print(check2)


# test()


# num1 = 4
# num2 = num1 + 1
# num1 = 2
# print(num1, num2)

# num1, num2 = 2, 6
# num1, num2 = num2, num1 + 2
# print(num1, ",", num2)

# num1, num2 = 2, 3
# num3, num2 = num1, num2 + 1
# print(num1, num2, num3)

# num1 = 4
# num2 = 3
# num3 = 2

# num1 += num2 + num3
# print(num1)

# num1 = num1 ** (num2 + num3)
# print(num1)

# num1 **= num2 + num3
# print(num1)

# num1 = "5" + "5"
# print(num1)

# num1 = 2 + 9 * ((3 * 12) - 8) / 10
# print(num1)


# Degree Celsius to Degree Fahrenheit

# C = float(input("What is the temperature in degree Celcius? "))
# F = float(0)


# def change():
#     F = (C * (9 / 5)) + 32

#     if F >= 100:
#         print("It is too hot! 🔥")
#     elif F <= 99 and F >= 90:
#         print("It is warm weather! 🌵")
#     elif F < 90 and F > 68:
#         print("It is good weather! 😎")
#     elif F <= 68 and F >= 66:
#         print("It is cold weather! 🌨")
#     elif F <= 65:
#         print("It is too cold! ⛄")
#     print("The temperature in Fahrenheit is:", F, "°F")


# change()


# To calculate the number of days to complete a job by three persons: A, B, C together

# from fraction import Fraction

# A = int(input("The number of days required to done the job by A: "))
# B = int(input("The number of days required to done the job by B: "))
# C = int(input("The number of days required to done the job by C: "))

# total_days = (A * B * C) / ((A*B) + (B*C) + (C*A))
# rounded_total_days = round(total_days, 2)

# print("The total number of days required to done the job by all three persons =", Fraction(rounded_total_days))


# Calculator

# from fraction import Fraction

# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))

# operator = input("Choose operator [+, -, *, /]: ")

# if operator == "+":
#   print(num1 + num2)

# elif operator == "-":
#   print(num1 - num2)

# elif operator == "*":
#   print(num1 * num2)

# elif operator == "/":
#   print(round((num1 / num2), 2))

#   if num1 / num2 < 1:
#     print(Fraction(round((num1 / num2), 2)))


# Repeat messages

# n = int(input("Enter how many times you want me say GOOD MORNING to you: "))

# for i in range(n):
#     print("GOOD MORNING!")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# average = round((num1 + num2 + num3) / 3, 2)
# print(average)

r = int(input("radius: "))
units = input("select units: ").lower()

pi = 3.1415926535 or 22 / 7

volume = (4 / 3) * pi * (r**3)

print("The volume of sphere with the radius", r, units, "is=", volume, "cubic", units)
