# mutable = changeable, immutable = not able to change
# mutable = everything except those below
# immutable = tuples, strings, integers, booleans, floats

a = []
b = a

a.append(35)  # both a and b add 35

print(id(a))  # Where in memory this list is
print(id(b))  # Where in memory this list is

c = "hello"
d = c

c = c + "world"

print(c)  # hello world
print(d)  # hello
