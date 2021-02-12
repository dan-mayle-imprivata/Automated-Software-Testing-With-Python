class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    def __repr__(self):
        return f"<Person {self.name}, {self.age}>"


bob = Person("Bob", 35)
print(bob)
# if using __str__
# Person Bob, 35 years old

# if using __repr__
# <Person (Bob, 35)>
