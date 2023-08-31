from project.car_manager import Car

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("BMW", "E46", 5.5, 63)

    def test_constructor(self):
        # "BMW", "E46", 5.5, 63
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("E46", self.car.model)
        self.assertEqual(5.5, self.car.fuel_consumption)
        self.assertEqual(63, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_to_rice_exception(self):
        expected = "Make cannot be null or empty!"
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual(expected, str(ex.exception))

    def test_model_setter_to_rice_exception(self):
        expected = "Model cannot be null or empty!"
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_consumption_setter(self):
        expected = "Fuel consumption cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_capacity_setter(self):
        expected = "Fuel capacity cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_amount_setter(self):
        expected = "Fuel amount cannot be negative!"
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual(expected, str(ex.exception))

    def test_refuel_with_invalid_fuel_amount(self):
        expected = "Fuel amount cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(expected, str(ex.exception))

    def test_refuel_new_quantity_is_less_than_tank_capacity(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_new_quantity_is_greater_or_equal_than_tank_capacity(self):
        self.car.refuel(100)
        self.assertEqual(63, self.car.fuel_amount)

    def test_drive_raise_exception(self):
        expected = "You don't have enough fuel to drive!"
        self.car.fuel_amount = 30
        self.car.fuel_consumption = 10
        with self.assertRaises(Exception) as ex:
            self.car.drive(301)
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(30, self.car.fuel_amount)

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 30
        self.car.fuel_consumption = 10
        self.car.drive(200)
        self.assertEqual(10, self.car.fuel_amount)
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    main()
