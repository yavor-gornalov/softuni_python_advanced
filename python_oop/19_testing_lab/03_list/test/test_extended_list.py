from project.extended_list import IntegerList

from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4.5)

    def test_initialized_correctly(self):
        expected = [1, 2, 3]
        self.assertEqual(expected, self.list._IntegerList__data)

    def test_index_error_exceptions(self):
        expected_message = "Index is out of range"
        expected_data = [1, 2, 3]

        with self.assertRaises(IndexError) as ie:
            self.list.get(3)
        self.assertEqual(expected_message, str(ie.exception))
        self.assertEqual(expected_data, self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(3)
        self.assertEqual(expected_message, str(ie.exception))
        self.assertEqual(expected_data, self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ie:
            self.list.insert(3, 4)
        self.assertEqual(expected_message, str(ie.exception))
        self.assertEqual(expected_data, self.list._IntegerList__data)

    def test_value_error_exceptions(self):
        expected_message = "Element is not Integer"
        expected_data = [1, 2, 3]

        with self.assertRaises(ValueError) as ve:
            self.list.add(3.5)
        self.assertEqual(expected_message, str(ve.exception))
        self.assertEqual(expected_data, self.list._IntegerList__data)

        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, 3.5)
        self.assertEqual(expected_message, str(ve.exception))
        self.assertEqual(expected_data, self.list._IntegerList__data)

    def test_add_integer_value(self):
        self.list.add(5)
        expected_data = [1, 2, 3, 5]
        self.assertEqual(expected_data, self.list._IntegerList__data)

    def test_get_element_from_valid_index(self):
        self.assertEqual(2, self.list.get(1))

    def test_remove_element_from_valid_index(self):
        self.assertEqual(2, self.list.remove_index(1))
        expected_data = [1, 3]
        self.assertEqual(expected_data, self.list._IntegerList__data)

    def test_insert_valid_element_to_valid_index(self):
        expected_data = [1, 4, 2, 3]
        self.list.insert(1, 4)
        self.assertEqual(expected_data, self.list._IntegerList__data)

    def test_get_data_method(self):
        expected_data = [1, 2, 3]
        self.assertEqual(expected_data, self.list.get_data())

    def test_get_biggest(self):
        expected_el = 3
        self.assertEqual(expected_el, self.list.get_biggest())

    def test_get_index(self):
        expected_idx = 0
        self.assertEqual(expected_idx, self.list.get_index(1))


if __name__ == "__main__":
    main()
