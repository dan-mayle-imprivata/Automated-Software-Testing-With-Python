# instance method will always have function with self as argument.
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")


# Call the method
# Method 1
test = ClassTest()
test.instance_method()

# Method 2
ClassTest.instance_method(test)
