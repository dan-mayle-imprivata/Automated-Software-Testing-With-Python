class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = self

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)  # BookShelf with 2 books.

print(shelf.books)  # Will give you all the books stored in the shelf


# Composition used a lot more than inheritance
# Used for when you want to say a BookShelf has many books.
