class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.name)  # "Rolf"
print(student.grades)  # (90, 90, 93, 78, 90)

# To call a method in a class

student = Student()
print(student.average_grade())  # 88.2
