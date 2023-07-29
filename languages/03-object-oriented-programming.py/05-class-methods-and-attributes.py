
""" class Car:
    number_of_cars = 0 # class attribute

    def __init__(self, make, model, year): # instance attributes
        self.make = make
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    @classmethod
    def update_number_of_cars(cls, number):
        cls.number_of_cars = number
        print("running class method")

    def myfunc(self): # instance method
        print("Hello my name is " + self.make + " " + self.model + " " + str(self.year))

Car.number_of_cars += 3
print(Car.number_of_cars)

c1 = Car("Ford", "Mustang", 1964)
c2 = Car("Ford", "Mustang", 1964)
print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars) """


class Circle:
    pi = 3.14 # class attribute

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** radius)

    @classmethod
    def circumference(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_circumference(cls, radius):
        return cls.area(radius), cls.circumference(radius)

print(Circle.get_area_and_circumference)

