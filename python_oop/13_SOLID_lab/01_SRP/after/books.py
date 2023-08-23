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

    def __find_book(self, book_title):
        for current_book in self.books:
            if current_book.title == book_title:
                return current_book

    def add_book(self, book: Book):
        if self.__find_book(book.title):
            raise ValueError("This book already exists")
        self.books.append(book)
        return f"The book '{book.title}' successfully added"

    def remove_book(self, book_name):
        current_book = self.__find_book(book_name)
        if not current_book:
            raise ValueError(f"The book '{book_name}' does not exit")
        self.books.remove(current_book)
        return f"The book '{book_name}' successfully removed"

    def get_info(self):
        books = '\n'.join([f"{b.title} by {b.author} - {b.pages}" for b in self.books])
        result = f"Library: {self.location}\n{books}"
        return result


book = Book("My First Book", "Me", 100)
book2 = Book("My Second Book", "Me", 100)
book3 = Book("My Third Book", "Me", 100)

# print(book.open_book())
# print(book.goto_page(99))
# print(book.next_page())
# print(book.next_page())
# print(book.previous_page())
# print(book.close_book())

library = Library("University")
library.add_book(book)
try:
    library.add_book(book)
except ValueError as e:
    print(*e.args)
library.add_book(book2)
library.add_book(book3)
print(library.get_info())
try:
    library.remove_book("My Book")
except ValueError as e:
    print(*e.args)

print(library.remove_book("My Second Book"))
print(library.get_info())
