from project.truck_driver import TruckDriver

from unittest import TestCase, main


class TruckDriverTests(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("George", 10)

    def test_constructor(self):
        self.assertEqual("George", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertFalse(self.driver.available_cargos)
        self.assertFalse(self.driver.earned_money)
        self.assertFalse(self.driver.miles)

    def test_negative_money_earned_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money -= 1
        expected = "George went bankrupt."
        self.assertEqual(expected, str(ve.exception))

    def test_add_cargo_offer(self):
        result = self.driver.add_cargo_offer("Nevada", 1000)
        expected = "Cargo for 1000 to Nevada was added as an offer."
        self.assertEqual(expected, result)
        self.assertEqual({"Nevada": 1000}, self.driver.available_cargos)

    def test_add_cargo_offer_if_location_exists(self):
        self.driver.add_cargo_offer("Nevada", 1000)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Nevada", 1200)
        expected = "Cargo offer is already added."
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Nevada": 1000}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_if_no_cargos_raises_value_error(self):
        result = self.driver.drive_best_cargo_offer()
        expected = "There are no offers available."
        self.assertEqual(expected, result)

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Nevada", 100)
        self.driver.add_cargo_offer("Colorado", 50)

        result = self.driver.drive_best_cargo_offer()
        expected = "George is driving 100 to Nevada."
        self.assertEqual(expected, result)
        self.assertEqual(1000, self.driver.earned_money)
        self.assertEqual(100, self.driver.miles)

    def test_check_activities_by_driving_over_10k_miles(self):
        self.driver.add_cargo_offer("Canada", 10000)
        result = self.driver.drive_best_cargo_offer()
        expected = "George is driving 10000 to Canada."
        self.assertEqual(expected, result)
        money_earned = 10000 * 10 - 40 * 20 - 10 * 45 - 6 * 500 - 7500
        self.assertEqual(money_earned, self.driver.earned_money)

    def test_representation(self):
        self.driver.add_cargo_offer("Canada", 10000)
        self.driver.drive_best_cargo_offer()
        expected = f"George has 10000 miles behind his back."
        self.assertEqual(expected, str(self.driver))


if __name__ == "__main__":
    main()
