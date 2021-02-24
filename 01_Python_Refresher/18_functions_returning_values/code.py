def add(x, y):
    return x + y


add(5, 8)  # 13 but not printed
result = add(5, 8)  # result = 13
print(result)  # prints 13 once


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 3)
print(result)
