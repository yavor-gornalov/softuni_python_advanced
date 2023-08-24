from typing import List


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def __get_current_page(self, page):
        if page <= 0 or page > self.pages:
            return f"Invalid page number"
        self.current_page = page
        return f"You opened the book - {self.title} at page {self.current_page}"

    def open_book(self):
        return self.__get_current_page(1)

    def next_page(self):
        return self.__get_current_page(self.current_page + 1)

    def previous_page(self):
        return self.__get_current_page(self.current_page - 1)

    def goto_page(self, page):
        return self.__get_current_page(page)

    def close_book(self):
        self.current_page = 0
        return f"You closed the book - {self.title} by {self.author}"


class Library:
    def __init__(self, location):
        self.books: List[Book] = []
        self.location = location

    def _get_book(self, book_title):
        for current_book in self.books:
            if current_book.title == book_title:
                return current_book
        raise ValueError(f"The book '{book_title}' does not exit")

    def find_book(self, book_title):
        try:
            self._get_book(book_title)
            return f"The book {book_title} founded"
        except ValueError:
            return f"No such book in the Library"

    def add_book(self, book: Book):
        try:
            self._get_book(book.title)
            return "This book already exists"
        except ValueError:
            self.books.append(book)
            return f"The book '{book.title}' successfully added"

    def remove_book(self, book_title):
        try:
            book = self._get_book(book_title)
            self.books.remove(book)
            return f"The book '{book_title}' successfully removed"
        except ValueError:
            return f"The book '{book_title}' does not exit"

    def get_info(self):
        books = '\n'.join([f"{b.title} by {b.author} - {b.pages}" for b in self.books])
        result = f"Library: {self.location}\n{books}"
        return result


my_book = Book("My First Book", "Me", 100)
my_book2 = Book("My Second Book", "Me", 100)
my_book3 = Book("My Third Book", "Me", 100)

library = Library("University")
library.add_book(my_book)
print(library.add_book(my_book))
print(library.add_book(my_book2))
print(library.add_book(my_book3))
print(library.get_info())
print(library.remove_book("My Book"))
print(library.remove_book("My Second Book"))
print(library.get_info())

print(library.find_book("My Third Book"))
print(library.find_book("My Second Book"))
book = library._get_book("My Third Book")
print(my_book.open_book())
print(my_book.goto_page(99))
print(my_book.next_page())
print(my_book.close_book())
