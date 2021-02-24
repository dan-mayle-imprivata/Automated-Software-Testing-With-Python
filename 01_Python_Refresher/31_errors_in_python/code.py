def divide(dividend, divisor):
    if divisor == 0:
        # One of many built in errors
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


grades = [78, 99, 85, 100]
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:  # e will contain the error, can be called anything
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you")
