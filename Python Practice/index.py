# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display_info(self):
#         print(f"This is a {self.make} {self.model}.")


# car1 = Vehicle("Toyota", "Camry")
# car2 = Vehicle("Honda", "Civic")

# car1.display_info()
# car2.display_info()


# class Dog():
#   attr1 = "mammal"
#   attr2 = "dog"
#   d = 45

#   def fun(self):
#     print("I'm a", self.attr1)
#     print("I'm a", self.attr2)

# Rodger = Dog()

# print(Rodger.attr1)
# Rodger.fun()

# print(Rodger.d)

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello " + self.name)

name = input("What is your name? ")
p = Person(name)
p.say_hi()