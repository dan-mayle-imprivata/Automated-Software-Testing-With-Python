class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# To call a method in a class
student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (100, 100, 93, 78, 90))

print(student.name)  # Bob
print(student2.name)  # Rolf
print(student.average_grade())  # 88.2
