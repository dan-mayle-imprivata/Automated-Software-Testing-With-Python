def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
#(1, 3, 5)
#{'name': 'Bob', 'age': 25}


def myfunction(**kwargs):
    print(kwargs)


# must be dictionary after **
myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error
