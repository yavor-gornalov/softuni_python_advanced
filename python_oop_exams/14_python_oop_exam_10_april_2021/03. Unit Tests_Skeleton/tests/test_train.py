from project.train.train import Train

from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("My Train", 5)

    def test_constructor(self):
        self.assertEqual("My Train", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_method_happy_path(self):
        result = self.train.add("John")
        expected = "Added passenger John"
        self.assertEqual(expected, result)
        self.assertEqual(["John"], self.train.passengers)

    def test_add_over_capacity_raises_ve(self):
        self.train.capacity = 1
        self.train.add("John")
        with self.assertRaises(ValueError) as ve:
            self.train.add("George")
        expected = "Train is full"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(["John"], self.train.passengers)

    def test_add_passenger_already_existing_raises_ve(self):
        self.train.add("John")
        with self.assertRaises(ValueError) as ve:
            self.train.add("John")
        expected = "Passenger John Exists"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(["John"], self.train.passengers)

    def test_remove_passenger_happy_path(self):
        self.train.add("John")
        self.train.add("George")
        self.assertEqual(["John", "George"], self.train.passengers)

        result = self.train.remove("John")
        expected = "Removed John"
        self.assertEqual(expected, result)
        self.assertEqual(["George"], self.train.passengers)

    def test_remove_not_existing_passenger_raises_ve(self):
        self.train.add("John")
        self.assertEqual(["John"], self.train.passengers)

        with self.assertRaises(ValueError) as ve:
            self.train.remove("George")
        expected = "Passenger Not Found"
        self.assertEqual(expected, str(ve.exception))


if __name__ == "__main__":
    main()
