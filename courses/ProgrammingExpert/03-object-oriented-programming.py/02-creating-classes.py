class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def myfunc(self):
        print("Hello my name is " + self.make + " " + self.model + " " + str(self.year))

class Fruit:
    def __init__(self, name, color, calories):
        self.name = name
        self.color = color
        self.calories = calories

    def myfunc(self):
        print("Hello my name is " + self.name + " and my color is " + self.color)


p1 = Person("John", 36)
print(p1.name)

c1 = Car("Ford", "Mustang", 1964)
print(c1.myfunc())

f = Fruit("Apple", "Red", 50)
print(f.myfunc())

