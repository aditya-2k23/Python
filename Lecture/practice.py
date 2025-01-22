# marks = list(map(int, input().split()))

# total = sum(marks)
# average = total / len(marks)

# print(f"Average Grade: {average}")

# if average >= 90 and average <= 100:
#     print("Letter Grade: A")
# elif average >= 80 and average < 90:
#     print("Letter Grade: B")
# elif average >= 70 and average < 80:
#     print("Letter Grade: C")
# elif average >= 60 and average < 70:
#     print("Letter Grade: D")
# else:
#     print("Letter Grade: F")

for i in range(1, 101):
    if (i % 15 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
