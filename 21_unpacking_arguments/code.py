def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(1, 3, 5))  # 15


def add(x, y):
    return x + y


nums = [3, 5]

add(nums)  # Will pass [3,5] to x and nothing to y resulting in an error

add(*nums)  # will use 3 for x and 5 for y. Equals 8.

nums2 = {"x": 15, "y": 25}
print(add(**nums2))  # will add the value to each variable. Equals 40.
