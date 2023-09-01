from project.vehicle import Vehicle

from unittest import TestCase, main


class VehicleTests(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(10, 100)

    def test_constructor(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel(self):
        expected = "Not enough fuel"
        kilometers = 10
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers)
        self.assertEqual(expected, str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(8)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_with_to_much_fuel(self):
        expected = "Too much fuel"
        self.vehicle.drive(8)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10.1)
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_with_proper_quantity(self):
        self.vehicle.drive(8)
        self.vehicle.refuel(10)
        self.assertEqual(10, self.vehicle.fuel)

    def test_object_representation(self):
        expected = (f"The vehicle has 100 horse power with"
                    f" 10 fuel left and 0.5 fuel consumption")

        self.vehicle.fuel_consumption = 0.5
        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == "__main__":
    main()
