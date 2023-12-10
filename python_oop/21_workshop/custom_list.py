"""
Workshop - CustomList
Demonstrative code and unittests designed by Ines Kenova
"""

from copy import deepcopy
from typing import Optional, Any, Dict
from collections.abc import Iterable


class CustomList:
    def __init__(self, *args) -> None:
        self.__values = list(args)

    def append(self, value: Any) -> Any:
        self.__values.append(value)
        return self.__values

    def __check_index_type(self, index: int) -> None:
        if not isinstance(index, int):
            raise ValueError("Invalid index type. You must pass an integer")

    def remove(self, index: int) -> Optional[Any]:
        self.__check_index_type(index)

        try:
            return self.__values.pop(index)
        except IndexError:
            raise IndexError("Invalid index")

    def save_remove(self, index: int) -> Optional[Any]:
        self.__check_index_type(index)

        try:
            return self.__values.pop(index)
        except IndexError:
            return None

    def get(self, index: int, default_val: Optional[Any] = None):
        self.__check_index_type(index)

        try:
            return self.__values[index]
        except IndexError:
            if default_val is None:
                return None
            return default_val

    def extend(self, value: Any, *args):
        if isinstance(value, Iterable):
            self.__values.extend(value)
        else:
            self.__values.append(value)
        self.__values.extend(args)
        return self.__values

    def insert(self, index: int, value: Any):
        self.__check_index_type(index)

        try:
            self.__values.insert(index, value)
            return self.__values
        except IndexError:
            raise IndexError("Invalid index")

    def pop(self):
        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index(self, value: Any):
        return self.__values.index(value)

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return list(reversed(self.__values))

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)

    def dictionize(self) -> Dict[Any, Any]:
        result = {}
        for index in range(0, len(self.__values), 2):
            key = self.__values[index]
            try:
                value = self.__values[index + 1]
            except IndexError:
                value = " "

            result[key] = value
        return result

    def move(self, amount: int):
        self.__check_index_type(amount)
        first_part = self.__values[:amount]
        second_part = self.__values[amount:]
        self.__values = second_part + first_part
        return self.__values

    def sum(self) -> float:
        result = 0

        for el in self.__values:
            if isinstance(el, int) or isinstance(el, float):
                result += el
            else:
                result += len(el)

        return result

    def overbound(self) -> int:
        biggest_index = None
        max_value = float('-inf')

        for index in range(len(self.__values)):
            element = self.__values[index]
            if isinstance(self.__values[index], Iterable):
                element = len(self.__values[index])

            if element > max_value:
                max_value = element
                biggest_index = index

        return biggest_index

    def underbound(self) -> int:
        smallest_index = None
        max_value = float('inf')

        for index in range(len(self.__values)):
            element = self.__values[index]
            if isinstance(self.__values[index], Iterable):
                element = len(self.__values[index])

            if element < max_value:
                max_value = element
                smallest_index = index

        return smallest_index


from unittest import TestCase, main

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.cl = CustomList(5, "asd", 3.6)

    def test_initialise(self):
        cl = CustomList()
        self.assertEqual(cl._CustomList__values, [])

        cl = CustomList(5, "asd", 3.6)
        self.assertEqual(cl._CustomList__values, [5, "asd", 3.6])

    def test_append_no_argument_raises(self):
        # We do not test that usually it is just an example
        with self.assertRaises(TypeError) as ex:
            self.cl.append()
        self.assertIn("missing 1 required positional argument", str(ex.exception))

    def test_append_adds_element_to_the_end(self):
        # Pre preparation (arrange), assumptions
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.append(100)

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, 100])
        self.assertEqual(self.cl._CustomList__values[-1], 100)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_append_element_to_empty_list(self):
        cl = CustomList()
        self.assertEqual(cl._CustomList__values, [])

        cl.append(5)

        self.assertEqual(cl._CustomList__values, [5])

    def test_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.remove(invalid_index)
            self.assertIn("Invalid index type", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_remove_invalid_index_raises(self):
        # Which means the last index is 2, or -3
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        with self.assertRaises(IndexError) as ex:
            self.cl.remove(3)
        self.assertIn("Invalid index", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.cl.remove(-4)
        self.assertIn("Invalid index", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_remove_multiple_same_elements_are_not_removed(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "asd"])

        result = self.cl.remove(1)
        self.assertEqual(result, "asd")
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 3.6, "asd"])

    def test_remove_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.remove(1)

        self.assertEqual(result, "asd")
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual(self.cl._CustomList__values, [5, 3.6])

    def test_remove_minus_index_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.remove(-1)

        self.assertEqual(result, 3.6)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual(self.cl._CustomList__values, [5, "asd"])

    def test_save_remove_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.save_remove(invalid_index)
            self.assertIn("Invalid index type", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_save_remove_invalid_index_returns_none(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.save_remove(12)

        self.assertIsNone(result)

    def test_save_remove_minus_index_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.save_remove(-1)

        self.assertEqual(result, 3.6)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual(self.cl._CustomList__values, [5, "asd"])

    def test_get_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.get(invalid_index)
            self.assertIn("Invalid index type", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_get_invalid_index_returns_none(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.get(3)
        self.assertIsNone(result)

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_get(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.get(1)
        self.assertEqual(result, "asd")

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_get_with_optional_invalid_index_retunrs_optional_arg(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.get(11, "Test")
        self.assertEqual(result, "Test")

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_extend(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.extend(1, 2, 3)

        self.assertEqual(len(self.cl._CustomList__values), 6)
        self.assertEqual([5, "asd", 3.6, 1, 2, 3], self.cl._CustomList__values)

        self.assertEqual(result, self.cl._CustomList__values)

    def test_extend_with_iterable(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.extend([1, 1], 2, 3)
        self.assertEqual(len(self.cl._CustomList__values), 7)
        self.assertEqual([5, "asd", 3.6, 1, 1, 2, 3], self.cl._CustomList__values)

        self.assertEqual(result, self.cl._CustomList__values)

    def test_insert_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.insert(invalid_index, "a")
            self.assertIn("Invalid index type", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_invalid_index_appends_the_value(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.insert(55, "a")

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "a"])

    def test_insert(self):
        # insert at 0
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.insert(0, 100)

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [100, 5, "asd", 3.6])
        self.assertEqual(result, self.cl._CustomList__values)

        # insert in the middle
        result = self.cl.insert(2, 90)

        self.assertEqual(len(self.cl._CustomList__values), 5)
        self.assertEqual(self.cl._CustomList__values, [100, 5, 90, "asd", 3.6])
        self.assertEqual(result, self.cl._CustomList__values)

    def test_pop_empty_list_raises(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)

        with self.assertRaises(IndexError) as ex:
            cl.pop()
        self.assertIn('empty list', str(ex.exception))

        self.assertEqual([], cl._CustomList__values)

    def test_pop_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.pop()

        self.assertEqual(3.6, result)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual(self.cl._CustomList__values, [5, "asd"])

    def test_clear(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.clear()
        self.assertIsNone(result)

        self.assertEqual(len(self.cl._CustomList__values), 0)
        self.assertEqual(self.cl._CustomList__values, [])

    def test_index_invalid_element_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        with self.assertRaises(Exception) as ex:
            self.cl.index(55)

        self.assertIn("not in list", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_index_returns_value(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "asd"])

        result = self.cl.index("asd")
        self.assertEqual(result, 1)

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "asd"])

    def test_count(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "asd"])

        result = self.cl.count(6)
        self.assertEqual(result, 0)

        result = self.cl.count(5)
        self.assertEqual(result, 1)

        result = self.cl.count("asd")
        self.assertEqual(result, 2)

    def test_reverse_returns_reversed_list_values_list_remains_unchanged(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.reverse()

        # List values remains unchanged
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        self.assertEqual(result, [3.6, "asd", 5])

    def test_copy_returns_copy_of_the_list(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.copy()

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        self.assertNotEqual(id(self.cl._CustomList__values), id(result))
        self.assertEqual(result, [5, "asd", 3.6])

    def test_copy_nested_structures_are_copies_not_references(self):
        self.cl.append([1, 2, 3])
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, [1, 2, 3]])

        result = self.cl.copy()

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, [1, 2, 3]])

        self.assertNotEqual(id(self.cl._CustomList__values), id(result))
        self.assertEqual(result, [5, "asd", 3.6, [1, 2, 3]])

        last_ref_el = self.cl._CustomList__values[-1]
        self.assertEqual(last_ref_el, [1, 2, 3])
        self.assertNotEqual(id(last_ref_el), id(result[-1]))

    def test_size(self):
        cl = CustomList()
        self.assertEqual(len(cl._CustomList__values), 0)

        result = cl.size()

        self.assertEqual(result, 0)

        self.assertEqual(len(self.cl._CustomList__values), 3)
        result = self.cl.size()

        self.assertEqual(result, 3)

    def test_add_first(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.add_first(100)
        self.assertIsNone(result)

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [100, 5, "asd", 3.6])

        cl = CustomList()
        self.assertEqual(len(cl._CustomList__values), 0)

        result = cl.add_first(100)

        self.assertEqual(cl._CustomList__values, [100])

    def test_dictionize(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.dictionize()
        self.assertEqual(result, {5: "asd", 3.6: " "})

        self.cl.append(100)
        result = self.cl.dictionize()
        self.assertEqual(result, {5: "asd", 3.6: 100})

    def test_move(self):
        self.cl.append(100)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, 100])

        result = self.cl.move(2)

        self.assertEqual(self.cl._CustomList__values, [3.6, 100, 5, "asd"])

        self.assertEqual(result, [3.6, 100, 5, "asd"])

    def test_move_larger_amount_than_the_list(self):
        self.cl.append(100)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, 100])

        result = self.cl.move(5)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, 100])
        self.assertEqual(result, [5, "asd", 3.6, 100])

    def test_invalid_amount_type(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.move(invalid_index)
            self.assertIn("Invalid index type", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_sum(self):
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])
        result = self.cl.sum()
        self.assertEqual(result, 11.6)

    def test_overbound(self):
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.overbound()
        self.assertEqual(result, 0)

        self.cl.append("123456")
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "123456"])

        result = self.cl.overbound()
        self.assertEqual(result, 3)

    def test_underbound(self):
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.underbound()
        self.assertEqual(result, 1)

        self.cl.append("a")
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "a"])

        result = self.cl.underbound()
        self.assertEqual(result, 3)


if __name__ == "__main__":
    main()
