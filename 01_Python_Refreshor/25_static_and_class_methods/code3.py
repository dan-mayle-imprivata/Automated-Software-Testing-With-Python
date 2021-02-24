class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type},weighing {self.weight} grams>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


book = Book("Harry Potter", "hardcover", 1500)

book2 = Book.hardcover("Harry Potter 2", 1500)

light = Book.paperback("Python 101", 600)

print(light)  # <Book Python 101, paperback,weighing 600 grams>

print(book2)  # <Book Harry Potter 2, hardcover,weighing 1600 grams>

print(Book.TYPES)  # ("hardcover", "paperback")

print(book.name)  # "Harry Potter"

print(book)  # <Book Harry Potter, hardcover,weighing 1500 grams>
