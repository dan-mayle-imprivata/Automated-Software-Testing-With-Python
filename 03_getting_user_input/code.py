name = input("Enter your name: ")
print(name)

# Math Input
size_input = input("How big is your house in square feet: ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(square_meters)

# Using F string and 2f (2 decimal places only)
print(f"{square_feet} square feet is {square_meters:.2f} square meters")
