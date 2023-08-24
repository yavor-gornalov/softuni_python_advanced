from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class DOSFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.content[0:15] + '...'}"


class HTMLFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"<h1>\n{' ' * 4 + book.title}\n</h1>\n<p>\n{' ' * 4 + book.content}\n</p>"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


my_book = Book("My Book", "This is a too long content for DOSFormatter!")
dos_printer = Printer(DOSFormatter())
web_printer = Printer(HTMLFormatter())

print(dos_printer.get_book(my_book))
print(web_printer.get_book(my_book))
