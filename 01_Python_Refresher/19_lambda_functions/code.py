def add(x, y):
    return x + y


print(add(5, 7))

# lambda version, (short function often with no name)

print((lambda x, y: x + y)(5, 7))

# More common lambda with name

# add = lambda x, y: x + y
# print(add(5,7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]  # More common
doubled2 = map(double, sequence)
doubled3 = [(lambda x: x * 2)(x) for x in sequence]  # Lambda verion
