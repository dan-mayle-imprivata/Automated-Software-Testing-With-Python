# list
l = ["Bob", "Rolf", "Anne"]

# tuple (Can't modify)
t = ("Bob", "Rolf", "Anne")

# set (Can't have duplicate elements, also don't keep order)
s = {"Bob", "Rolf", "Anne"}


print(l[0])
print(t[2])

# Change elements
l[0] = "Smith"

# Add elements to list
l.append("Smithy")
print(l)

# Add elements to set
s.add("Smith")
print(s)

# Remove
l.remove("Bob")
print(l)
