def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


# passing in a function as an argument
result = calculate(20, 4, operator=divide)
print(result)  # 5.0
