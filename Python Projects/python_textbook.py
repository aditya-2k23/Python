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


# VOLUME OF SPHERE CALCULATOR


# r = int(input("radius: "))
# units = input("select units: ").lower()

# pi = 3.1415926535 or 22 / 7

# volume = (4 / 3) * pi * (r**3)

# print("The volume of sphere with the radius", r, units, "is=", volume, "cubic", units)


# AGE CALCULATOR FROM NOW


# name = input("What is your name: ").title()
# age = int(input("Enter your age: "))

# number_of_years = 100 - age
# years_from_now = 2023 + number_of_years

# print(
#     "Your name is", name, "& your age is", age, "& you will turn 100 in", years_from_now
# )


# DETERMINE THE ENERGY

# m = int(input("Enter your mass: "))
# c = 3 * (10**8)

# e = m / 1000 * c

# print("You have capable energy of:", e, "Joules.")


# HEIGHT OF WINDOW


# import math

# length = int(input("Length of Ladder: "))
# angle = int(input("Angle formed by the ladder and the wall: "))
# radian = math.radians(angle)
# sin = math.sin(radian)

# height = round(length * sin, 2)
# print(
#     f"The height reached by the ladder having length {length} and angle {angle} is: {height}"
# )


# a = 110
# while a > 100:
#     print(a)
#     a -= 2

# for i in range(20, 30, 2):
#     print(i)

# country = "INDIA"
# for i in country:
#     print(i)

# i = 0; sum = 0
# while i < 9:
#     if i % 4 == 0:
#         sum = sum + i
#     i = i + 2
# print(sum)

# for x in range(1, 4):
#     for y in range(2, 5):
#         if x * y > 10:
#             break
#         print(x * y)

# var = 7
# while var > 0:
#     print ('Current variable value:', var)
#     var = var - 1
#     if var == 3:
#         break
#     else:
#         if var == 6:
#             var = var - 1
#             continue
#     print ("Good bye!")


# DRIVING LICENSE

# name = input("Enter your name: ").title()
# age = int(input("Enter your age: "))

# if age >= 18:
#     print(name, "you are eligible for driving license!, as your age", age, "is above the minimum age requirement.")
# else:
#     print(name, "you are not eligible for driving license!, as your age", age, "is below the minimum age requirement.")


# PRINT THE TABLE 

# num = int(input("Enter the number to display its table: "))

# for a in range(1,11):
#     print(num," × ",a," = ",(num*a))

