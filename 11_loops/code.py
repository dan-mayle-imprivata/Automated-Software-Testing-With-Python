# while loop

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# will print 1,2,3,

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

    # prints 1,2,4,5,6

    # With the continue statement we can stop the current iteration,
    #  and continue with the next:

    i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

    # for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# prints apple,banana,cherry

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# stops at apple

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

    # prints apple, cherry

    for x in range(6):
        print(x)

    # prints 1,2,3,4,5

    for x in range(2, 6):
        print(x)

# prints 2,3,4,5
# adding a third parameter will determine how much number increases by
