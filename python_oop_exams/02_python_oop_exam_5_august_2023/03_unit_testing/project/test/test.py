from project.second_hand_car import SecondHandCar

from unittest import TestCase, main


class SecondHandCarTests(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Tesla Model 3", "sedan", 100_000, 10_000.00)

    def test_constructor(self):
        self.assertEqual("Tesla Model 3", self.car.model)
        self.assertEqual("sedan", self.car.car_type)
        self.assertEqual(100_000, self.car.mileage)
        self.assertEqual(10_000.00, self.car.price)
        self.assertFalse(self.car.repairs)

    def test_change_car_price(self):
        self.car.price = 15_000
        self.assertEqual(15_000, self.car.price)

    def test_set_low_price_to_rice_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        expected = 'Price should be greater than 1.0!'
        self.assertEqual(expected, str(ve.exception))

    def test_change_milage(self):
        self.car.mileage = 10_000
        self.assertEqual(10_000, self.car.mileage)

    def test_set_low_milage_to_rice_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        expected = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected, str(ve.exception))

    def test_promotional_price_higher_than_current(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(10_000)
        expected = 'You are supposed to decrease the price!'
        self.assertEqual(expected, str(ve.exception))

    def test_promotional_price_happy_path(self):
        result = self.car.set_promotional_price(9999)
        expected = 'The promotional price has been successfully set.'
        self.assertEqual(expected, result)

    def test_need_impossible_repair(self):
        result = self.car.need_repair(5001, "engine replacement")
        expected = 'Repair is impossible!'
        self.assertEqual(expected, result)

    def test_need_repair(self):
        result = self.car.need_repair(5000, "engine replacement")
        expected = 'Price has been increased due to repair charges.'
        self.assertEqual(expected, result)
        self.assertEqual(15_000, self.car.price)
        self.assertEqual(['engine replacement'], self.car.repairs)

    def test_great_than_dunder_with_different_car_types(self):
        self.car2 = SecondHandCar("Tesla Model 3", "SUV", 100_000, 10_000.00)
        result = self.car > self.car2
        expected = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected, result)

    def test_great_than_dunder_with_same_car_types(self):
        self.car2 = SecondHandCar("Tesla Model 3", "sedan", 100_000, 15_000.00)
        self.assertFalse(self.car > self.car2)

    def test_str_dunder_(self):
        self.car.need_repair(2500, "engine replacement")
        expected = """Model Tesla Model 3 | Type sedan | Milage 100000km
Current price: 12500.00 | Number of Repairs: 1"""
        self.assertEqual(expected, str(self.car))


if __name__ == "__main__":
    main()
