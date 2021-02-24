def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)  # {"name":"Bob","age":25}


def named2(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named2(**details)  # Bob 25
