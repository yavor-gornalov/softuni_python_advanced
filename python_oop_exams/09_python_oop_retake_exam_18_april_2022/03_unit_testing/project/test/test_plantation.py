from project.plantation import Plantation

from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test_constructor(self):
        self.assertEqual(2, self.plantation.size)
        self.assertFalse(self.plantation.plants)
        self.assertFalse(self.plantation.workers)

    def test_size_setter_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        expected = "Size must be positive number!"
        self.assertEqual(expected, str(ve.exception))

    def test_hire_worker(self):
        result = self.plantation.hire_worker("Pesho")
        self.assertEqual(["Pesho"], self.plantation.workers)
        self.assertEqual("Pesho successfully hired.", result)

    def test_hire_worker_already_hired_expect_value_error(self):
        self.plantation.hire_worker("Gosho")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Gosho")
        expected = "Worker already hired!"
        self.assertEqual(expected, str(ve.exception))

    def test_len_dunder(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants["Gosho"] = "potatoes"
        self.assertEqual(8, len(self.plantation))
        self.plantation.plants["Pesho"] = "carrots"
        self.assertEqual(15, len(self.plantation))

    def test_planting_using_unknown_worker_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "potatoes")
        expected = "Worker with name Gosho is not hired!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_over_capacity_expect_value_error(self):
        self.plantation.size = 1
        self.plantation.hire_worker("Gosho")
        self.plantation.planting("Gosho", "potatoes")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "carrots")
        expected = "The plantation is full!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_more_than_one_plant(self):
        self.plantation.hire_worker("Gosho")
        result = self.plantation.planting("Gosho", "potatoes")
        self.assertEqual("Gosho planted it's first potatoes.", result)

        result = self.plantation.planting("Gosho", "carrots")
        self.assertEqual("Gosho planted carrots.", result)
        self.assertEqual({"Gosho": ["potatoes", "carrots"]}, self.plantation.plants)

    def test_str_method(self):
        self.plantation.size = 4
        self.plantation.hire_worker("Gosho")
        self.plantation.planting("Gosho", "potatoes")
        self.plantation.planting("Gosho", "carrots")
        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "pumpkins")

        expected = """Plantation size: 4
Gosho, Pesho
Gosho planted: potatoes, carrots
Pesho planted: pumpkins"""

        self.assertEqual(expected, str(self.plantation))

    def test_repr_method(self):
        self.plantation.size = 4
        self.plantation.hire_worker("Gosho")
        self.plantation.planting("Gosho", "potatoes")
        self.plantation.planting("Gosho", "carrots")
        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "pumpkins")

        expected = ("Size: 4\n"
                    "Workers: Gosho, Pesho")

        self.assertEqual(expected, repr(self.plantation))


if __name__ == "__main__":
    main()
