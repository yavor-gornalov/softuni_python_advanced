from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def is_book_available(self, author: str, book_name: str):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                return True
        return False

    def get_book_from_rented_books(self, book_name):
        for user, book_data in self.rented_books.items():
            if book_name in book_data:
                return book_data[book_name]

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if self.is_book_available(author, book_name):
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return_days = self.get_book_from_rented_books(book_name)
        if return_days:
            return f'The book "{book_name}" is already rented and will be available in {return_days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        if author not in self.books_available:
            self.books_available[author] = []
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
