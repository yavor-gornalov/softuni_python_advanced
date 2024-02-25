from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Station")

    def test_constructor(self):
        self.assertEqual("Station", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_short_name_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Sta"
        expected = "Name should be more than 3 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_name_empty_str_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = ""
        expected = "Name should be more than 3 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_change_name(self):
        self.station.name = "New Station"
        self.assertEqual("New Station", self.station.name)

    def test_new_arrival_on_board(self):
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.station.new_arrival_on_board("Train1")
        self.station.new_arrival_on_board("Train2")
        self.assertEqual(deque(["Train1", "Train2"]), self.station.arrival_trains)

    def test_train_has_arrived_first(self):
        self.station.new_arrival_on_board("Train1")
        result = self.station.train_has_arrived("Train1")
        expected = "Train1 is on the platform and will leave in 5 minutes."

        self.assertEqual(deque(["Train1"]), self.station.departure_trains)
        self.assertEqual(expected, result)

    def test_train_has_arrived_second(self):
        self.station.new_arrival_on_board("Train1")
        self.station.new_arrival_on_board("Train2")
        result = self.station.train_has_arrived("Train2")
        expected = "There are other trains to arrive before Train2."

        self.assertEqual(expected, result)
        self.assertEqual(deque(["Train1", "Train2"]), self.station.arrival_trains)

    def test_fill_departure_trains_sequence(self):
        self.station.new_arrival_on_board("Train1")
        self.assertEqual(deque(["Train1"]), self.station.arrival_trains)
        self.station.new_arrival_on_board("Train2")
        self.assertEqual(deque(["Train1", "Train2"]), self.station.arrival_trains)

        self.station.train_has_arrived("Train1")
        self.station.train_has_arrived("Train2")
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque(["Train1", "Train2"]), self.station.departure_trains)

    def test_train_has_left_successfully(self):
        self.station.new_arrival_on_board("Train1")
        self.station.new_arrival_on_board("Train2")
        self.station.train_has_arrived("Train1")
        self.station.train_has_arrived("Train2")

        result = self.station.train_has_left("Train1")
        self.assertEqual(True, result)
        self.assertEqual(deque(["Train2"]), self.station.departure_trains)

    def test_train_has_failed_to_left(self):
        self.station.new_arrival_on_board("Train1")
        self.station.new_arrival_on_board("Train2")
        self.station.train_has_arrived("Train1")
        self.station.train_has_arrived("Train2")

        result = self.station.train_has_left("Train2")
        self.assertEqual(False, result)
        self.assertEqual(deque(["Train1", "Train2"]), self.station.departure_trains)


if __name__ == "__main__":
    main()
