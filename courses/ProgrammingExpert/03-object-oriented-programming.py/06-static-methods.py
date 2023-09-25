class Student:
    def __init__(self, name, age, grade=[]):
        self.name = name
        self.age = age
        self.grades = grade
    @staticmethod
    def average_grade(grades):
        return sum(grades) / len(grades)


s1 = Student("Tim", 19, [90, 95, 100])
s2 = Student("Bill", 19, [80, 85, 90])

average = s1.average_grade(s1.grades)
print(average)


