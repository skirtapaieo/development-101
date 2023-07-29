
# Create a class called Student that has two attributes: name and grade.
class Student:
    all_students = []

    # Create a class variable called all_students that is a list of all the Student objects that have been created.
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self) # add the student to the list of all students


    @property # getter
    def grade(self):
        return self._grade

    @grade.setter # setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = new_grade

    @classmethod
    def get_best_student(cls):
        if cls.all_students == []:
            return max(cls.all_students, key=lambda student: student.grade)
        else:
            return None

    @classmethod
    def get_average_grade(cls):
        if cls.all_students:
            return sum(student.grade for student in cls.all_students) / len(cls.all_students)
        else:
            return -1 # if there are no students in the class

    @staticmethod
    def calculate_average_grade(students):
        if students:
            return sum(student.grade for student in students) / len(students)
        else:
            return -1
