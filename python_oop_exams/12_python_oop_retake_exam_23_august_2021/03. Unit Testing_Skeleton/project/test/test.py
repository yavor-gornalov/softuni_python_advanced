from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Lib")

        self.test_lib = Library("TestLib")
        self.test_lib.books_by_authors = {"author1": ["book1", "book2"], "author2": ["book3"]}
        self.test_lib.readers = {"reader1": [], "reader2": []}

    def test_constructor(self):
        self.assertEqual("Lib", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_empty_name_raises_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_change_name_with_non_empty_str(self):
        self.library.name = "Lib1"
        self.assertEqual("Lib1", self.library.name)

    def test_add_book_with_new_author(self):
        self.library.add_book("author", "book1")
        self.assertEqual({"author": ["book1"]}, self.library.books_by_authors)

    def test_add_another_book_from_existing_author(self):
        self.library.add_book("author", "book1")
        self.library.add_book("author", "book2")
        self.assertEqual({"author": ["book1", "book2"]}, self.library.books_by_authors)

    def test_add_duplicated_book(self):
        self.library.add_book("author", "book1")
        self.library.add_book("author", "book1")
        self.assertEqual({"author": ["book1"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("reader")
        self.assertEqual({"reader": []}, self.library.readers)

    def test_add_duplicated_reader(self):
        self.library.add_reader("reader")
        result = self.library.add_reader("reader")
        expected = "reader is already registered in the Lib library."
        self.assertEqual(expected, result)

    def test_rent_book_from_unknown_reader(self):
        result = self.test_lib.rent_book("reader3", "author1", "book1")
        expected = "reader3 is not registered in the TestLib Library."
        self.assertEqual(expected, result)

    def test_rent_book_with_unknown_author(self):
        result = self.test_lib.rent_book("reader1", "author3", "book1")
        expected = "TestLib Library does not have any author3's books."
        self.assertEqual(expected, result)

    def test_rent_book_with_unknown_title(self):
        result = self.test_lib.rent_book("reader1", "author1", "book3")
        expected = "TestLib Library does not have author1's \"book3\"."
        self.assertEqual(expected, result)

    def test_rent_book_happy_path(self):
        result = self.test_lib.rent_book("reader1", "author1", "book2")
        self.assertEqual(None, result)
        self.assertEqual([{'author1': 'book2'}], self.test_lib.readers["reader1"])
        self.assertEqual(["book1"], self.test_lib.books_by_authors["author1"])


if __name__ == "__main__":
    main()
