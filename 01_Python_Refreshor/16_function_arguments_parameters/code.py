def add(x, y):
    result = x + y
    print(result)


add(5, 3)  # 8


def say_hello(name, surname):
    print(f"Hello, {name} {surname}!")


# positional argument
say_hello("Bob", "Smith")  # Hello, Bob Smith!


def say_hello2(name, surname):
    print(f"Hello, {name} {surname}!")


# keyword argument
say_hello2(surname="Bob", name="Smith")  # Hello, Smith Bob!
