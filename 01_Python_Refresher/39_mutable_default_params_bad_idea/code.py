from typing import List


# the init has a param of List with default value of list (not good)
class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

# Both students will have 90 even though only Bob took the exam
