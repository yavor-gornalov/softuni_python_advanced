from unittest import TestCase, main
from project.toy_store import ToyStore


class ToyStoreTests(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_constructor(self):
        expected = dict.fromkeys(list('ABCDEFG'), None)
        self.assertEqual(expected, self.toy_store.toy_shelf)

    def test_add_toy_on_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("1", "Bear")
        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_on_taken_shelf(self):
        self.toy_store.toy_shelf["A"] = "Cow"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Bear")
        expected = "Shelf is already taken!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy(self):
        result = self.toy_store.add_toy("A", "Bear")
        expected = "Toy:Bear placed successfully!"
        self.assertEqual(expected, result)
        self.assertEqual(self.toy_store.toy_shelf["A"], "Bear")

    def test_remove_from_unknown_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("J", "Bear")
        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_unknown_toy(self):
        self.toy_store.add_toy("A", "Bear")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Cow")
        expected = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_known_toy_from_known_shelf(self):
        self.toy_store.add_toy("A", "Bear")
        self.assertEqual(self.toy_store.toy_shelf["A"], "Bear")
        result = self.toy_store.remove_toy("A", "Bear")
        expected = "Remove toy:Bear successfully!"
        self.assertEqual(expected, result)
        self.assertEqual(self.toy_store.toy_shelf["A"], None)


if __name__ == "__main__":
    main()
