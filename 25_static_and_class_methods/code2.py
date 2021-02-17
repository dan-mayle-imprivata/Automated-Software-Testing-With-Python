# class method (used more) and static method (used less)
class ClassTest:

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")


ClassTest.class_method()

ClassTest.static_method()
