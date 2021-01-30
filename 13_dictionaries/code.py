friend_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}

print(friend_ages["Adam"])  # 30

# Add an key/value
friend_ages["Bob"] = 20

# Change a key/value
friend_ages["Rolf"] = 21

# list with of dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 24},
    {"name": "Anne", "age": 24},
]

print(friends[1])  # {"name": "Adam", "age": 24}
print(friends[1]["name"])  # Adam

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(student)  # Rolf, Bob, Anne

# print every key value pair
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# print every key value pair (better way)
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# If statements
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student at this class")

# Values only
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
