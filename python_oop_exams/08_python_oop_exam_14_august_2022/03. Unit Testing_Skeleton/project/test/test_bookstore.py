from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(books_limit=5)

    def test_constructor(self):
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_set_to_0(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        expected = "Books limit of 0 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test_book_limit_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        expected = "Books limit of -1 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test_book_limit_positive_value(self):
        self.bookstore.books_limit = 7
        self.assertEqual(7, self.bookstore.books_limit)

    def test_receive_book(self):
        self.bookstore.receive_book("Godfather I", 1)
        result = self.bookstore.receive_book("Godfather I", 2)
        expected = "3 copies of Godfather I are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles["Godfather I"])

    def test_receive_book_raises_ex(self):
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather II", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Godfather III", 2)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Godfather I": 2, "Godfather II": 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_raises_non_existing_book_ex(self):
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather II", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Godfather III", 3)
        expected = "Book Godfather III doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_raises_not_enough_copies_ex(self):
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather II", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Godfather II", 3)
        expected = "Godfather II has not enough copies to sell. Left: 2"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_raises(self):
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather II", 2)
        result = self.bookstore.sell_book("Godfather II", 2)
        expected = "Sold 2 copies of Godfather II"
        self.assertEqual(expected, result)
        self.assertEqual({"Godfather I": 1, "Godfather II": 0}, self.bookstore.availability_in_store_by_book_titles)

    def test_len_dunder(self):
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather II", 2)
        self.bookstore.sell_book("Godfather II", 1)
        self.assertEqual(2, len(self.bookstore))

    def test_len_dunder_of_empty_bookstore(self):
        self.assertEqual(0, len(self.bookstore))

    def test_representation(self):
        self.bookstore.receive_book("Godfather I", 1)
        self.bookstore.receive_book("Godfather II", 2)
        self.bookstore.sell_book("Godfather II", 2)
        self.bookstore.receive_book("Godfather III", 3)
        self.bookstore.sell_book("Godfather III", 2)
        expected = """Total sold books: 4
Current availability: 2
 - Godfather I: 1 copies
 - Godfather II: 0 copies
 - Godfather III: 1 copies"""
        self.assertEqual(expected, str(self.bookstore))

    def test_representation_with_no_data(self):
        expected = """Total sold books: 0
Current availability: 0"""
        self.assertEqual(expected, str(self.bookstore))


if __name__ == "__main__":
    main()
