t = (5, 11)
x, y = t
print(x, y)  # 5, 11


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# [('Rolf', 96), ('Bob', 80), ('Anne', 100)]
print(list(student_attendance.items()))


for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# Rolf: 96
# Bob: 80
# Anne: 100

people = [("Bob", 42, "Mechanic"), ("James", 24,
                                    "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age:{age}, Profession:{profession}")

# Name: Bob, Age:42, Profession:Mechanic
# Name: James, Age:24, Profession:Artist
# Name: Harry, Age:32, Profession:Lecturer

person = ("Bob", 42, "Mechanic")
name, _, profession = person  # _ is used when you want to ignore variable

print(name, profession)  # Bob Mechanic

# Seperate into two lists
# * is used to gather all numbers except head (1st number)
head, *tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(tail)  # [2, 3, 4, 5]
