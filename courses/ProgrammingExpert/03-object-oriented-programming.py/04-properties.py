"""
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary   #private attribute indication, but still accessible

    def say_hello(self):
        print("Hello my name is " + self.name)

    def set_age(self,age):
        self.age = age

    def get_age(self):
        return self.age

    @property #
    def salary(self):
        return round(self.salary)

    @salary.setter
    def salary(self, salary):
        self.salary = salary """

class Time:
    def __init__(self, second):
        self._second = second

"""     @property
    def second(self, second):
        self._second = second

    @second.setter
    def second(self):
        return self._second
"""
"""
t = Time(54)
t.second = 23
print(t.second)

 """


