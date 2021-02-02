def add(x, y=8):
    print(x+y)


add(5)  # 13


# Don't do this

default_y = 3


def add2(x, y=defalut_y):
    sum = x + y
    print(sum)


add(2)  # 5
default_y = 4
add(2)  # 5
