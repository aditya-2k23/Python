# comments

# variables

# print('hello world')

# name = 'Temaroon Gaming'
# age = 25

# print(name)
# print(age)

# full_name = 'aditya'
# print(full_name)

# width, height = 400, 500
# print(width)
# print(height)
# print(width, ",", height)

# your_name = input('Please enter you name: ').title()
# print('Hi ' + your_name)

# num1 = input('Enter a number: ')
# num2 = input('Enter a number: ')
# print(int(num1) + int(num2))

# strings
# numbers
# int (1, 2, 3) float/decimals (0.2, 0.07) (numbers)

# strings 'hello', "cookie" => "hello-cookie"   {ignore = '-'}
# strings '10', "20" => 1020

# math operators +, -, /, //, *, **, %

# Tip Calculator

# food_amount = int(input('Enter food amount: 💲'))
# tip_percentage = int(input('Enter tip percentage: ')) / 100
# tip_amount = food_amount * tip_percentage
# total = food_amount + tip_amount
# print('-----------------------------------------')
# print("The tip amount is 💵: " + str(tip_amount))
# print("You have to pay a total of 💰: 💲" + str(total))
# print('-----------------------------------------')

# string formatting

# BOOLEAN
# IF THEN ELSE
# if withdrawal amount > balance:
#   don't allow withdraw
# else:
#   allow withdrawal

# baby weather app
# if it's raining outside, grab an umbrella
# otherwise, grab your sunglasses

# BOOLEAN (True, False)
# True
# False

# weather = input("How's the weather? ").lower()

# if weather == 'rain':
#     print('☔')

# elif weather == "cloudy" or "clouds" or "overcast":
#     print('☁')

# elif weather == "thunderstorm":
#     print('⛈')

# elif weather == "tornado" or "twister":
#     print('🌪')

# elif weather == "sunny":
#     print('☀')

# elif weather == "haze" or "fog" or "foggy":
#     print('🌫')

# else:
#     print('Invalid weather. What are you doing? HUH? BOZO++')

# comparison operators (==, <, >, <=, >=)

# grade app

# marks = int(input('Enter your marks: '))
#
# if marks >= 90:
#     print('A', 'Amazing!')
# elif marks >= 80:
#     print('B', 'Keep it up!')
# elif marks >= 70:
#     print('C', 'Good!')
# elif marks >= 60:
#     print('D', 'You can do better!')
# else:
#     print('F', '-', "Better luck next time!")

# def say_my_name():
#     print('John')
#     print('Apple')
#     print('Wick')
#     print('Orange')


# say_my_name()

# def say_my_name_2(name):
#     print(name)


# say_my_name_2('Katie')

# def greeting(greet, name):
#     print(f'{greet} 🙋‍♂️ {name}')


# greeting('Hi', 'Sir')

# import


# """
# Takes 2 integers, returns their sum
# # >>> sum(1, 2)
# 3
# """

# def s(a, b):
#     return a + b


# print(s(1, 2))

# Tip Calculator

# food_amount = int(input('Enter food amount: 💲'))
# tip_percentage = int(input('Enter tip percentage: ')) / 100
# tip_amount = food_amount * tip_percentage
# total = food_amount + tip_amount


# def calculate_food_total(food, tip_percentage):
# tip = food * (tip_percentage / 100)
# total = food + tip
# return total


# print(calculate_food_total(100, 10))
# print(calculate_food_total(food=100, tip_percentage=20))

# def weather_to_emoji(weather):
#     """
#     weather_to_emoji takes in 1 argument as a string
#     (expected inputs: 'rain', 'thunderstorm', 'cloudy')

#     >> weather_to_emoji('rain')
#     '☔'

#     >> weather_to_emoji('thunderstorm')
#     '⛈'

#     >> weather_to_emoji('sunny')
#     '🌞'
#     """
#     if weather == 'rain':
#         print('☔')

#     elif weather == "cloudy" or "clouds" or "overcast":
#         print('☁')

#     elif weather == "thunderstorm":
#         print('⛈')

#     elif weather == "tornado" or "twister":
#         print('🌪')

#     elif weather == "sunny":
#         print('☀')

#     elif weather == "haze" or "fog" or "foggy":
#         print('🌫')

#     else:
#         print('Invalid weather. What are you doing? HUH? BOZO++')


# weather_to_emoji('rain')

# def bigger_guy(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# print(bigger_guy(1, 6))

# lambda - anonymous function
# def sum1(a, b):
#     return a + b


# sum2 = lambda a, b: a + b
# print(sum2(int(input('Enter first number: ')), int(input('Enter second number: '))))

# LISTS (ARRAYS)
# fruits = ['🍎', '🍐', '🍊', '🍌', '🍪', 2, 5, 'hi', 8.5, True, [4, 3]]
# print(fruits)

# fruits.append('🍊')
# print(fruits)

# fruits.append('🍓')
# print(fruits)

# INDEXING
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# How to ALWAYS get the last item in an array?

# print(fruits[-1])

# SLICING
# print(fruits[0:2])  # First Inclusive, Second Exclusive
# print(fruits[0:4])
# print(fruits[0: len(fruits) - 1])
# print('Hi my name is Aditya'[0: 17])
# print(fruits[::-1])  # reverse the array

# DICTIONARIES 
# Key 👉 value
# Laptop 👉 Apple
# mutable (change-able)


# print(person['name'])
# print(person['shirt'])
# print(person['laptop'])


# def net_worth(person):
#     return person['assets'] - person['debt']


# def introducer():

# person = {
#     'name': 'Aditya',
#     'shirt': ('Orange',),
#     'laptop': 'HP',
#     'phone_number': '224-123-3456',
#     'assets': 1000,
#     'debt': 0,
#     'favorite_fruits': ['🍎', '🍌', '🍊'],
#     'networth': lambda: person['assets'] - person['debt']}

# print(
#     f"🧑 Hi my name is {person['name']}, \n👚 I am wearing a {person['shirt']} shirt, \n💻 The laptop I use to code is a {person['laptop']}, \n💰 My net worth is ${person['networth']()} USD, \n🍑 My favorite fruits are {person['favorite_fruits']}, \n📞 My phone number is {person['phone_number']}")

# print(list(person.values()))
# print(person.keys())


# introducer()

# TUPLES ()
# immutable
# numbers = [1, 2]
# print(numbers)
# print(type(numbers))
# print(numbers[0])

# SETS {} 👉 Used for getting unique stuff
# print({1, 2, 2, 2, 2})

# list1 = ['ruby', 'python', 'javascript']
# list2 = ['ruby', 'SQL', 'JAVA', 'javascript']

# programming_languages = set(list1 + list2)
# print(programming_languages)
# print('SQL' in programming_languages)   # 👉 True
# print('GO' in programming_languages)    # 👉 False


# SPECIAL KEYWORDS
# list, len, max, min, set, dict

# """
# Create a function unique, that
# takes in a list and returns only unique items

# >> unique(['ruby', 'ruby', 'python'])
# ['ruby', 'python']
# """


# def unique(languages):
#     return list(set(languages))

# unique = lambda languages: list(set(languages))


# print(unique(['ruby', 'ruby', 'python']))

# LOOPS
# fruits = ['🍎', '🍐', '🍊', '🍌', '🍪']
# for fruit in fruits:
#     print(fruit)

# TUPLE Unpacking
# for index, fruit in enumerate(fruits):
#     print('Fruit:', fruit, index)

# Do this five times
# for i in range(5):
#     print(i)

# Add 10 apples to the fruits list
# for _ in range(10):
#     fruits.append('🍎')

# print(fruits)

# While Loops

# qazi = 'sitting'
# while qazi != 'standing':
#     print('Get your fat butt up 🍑!')

# counter = 0
# while counter < 10:
#     print(counter)
#     # counter = counter + 1
#     counter += 1

# numbers = [1, 2, 3, 4, 5]

"""
>> double([1, 2, 3, 4, 5])
[2, 4, 6, 8, 10]
"""

# def double(numbers):
#     result = []
#     for number in numbers:
#         result.append(number * 2)

#     return result


# print(double([1, 2, 3]))

# """
# Count Words if given a string,
# should count & return the number of words

# phrase: str

# >> count_words('Hi my name is Qazi')
# 5
# """

# def count_words(phrase):
#     return len(phrase.split())


# print(count_words('Hi my name is Qazi cookies cream soda legendary'))

# """
# Create a function that given a list of numbers,
# it can return their sum

# >> sum_list([1, 2, 3])
# 6
# """


# def sum_list(numbers):
#     count = 0
    # for number in numbers:
    #     count += number

    # return count


# print(sum_list([1, 2, 3]))
# print(sum_list([1, 2, 3, 4]))

# find_max

# """
# >> find_max([1, 5, 10, 3])
# 10
# """


def find_max(numbers):
    current_max = numbers[0]


numbers = [1, 5, 10, 3]
current_max = 1  # numbers[0]
