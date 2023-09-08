from project.robot import Robot
from unittest import TestCase, main


class RobotTests(TestCase):
    def setUp(self) -> None:
        self.robot = Robot(1, 'Military', 2, 100)

    def test_constructor(self):
        self.assertEqual(1, self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(2, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertFalse(self.robot.hardware_upgrades)
        self.assertFalse(self.robot.software_updates)

    def test_robot_category_not_listed_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Unknown"
        expected = f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected, str(ve.exception))

    def test_set_robot_price_to_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -0.5
        expected = "Price cannot be negative!"
        self.assertEqual(expected, str(ve.exception))

    def test_upgrade_robot(self):
        result = self.robot.upgrade("RAM", 100)
        expected = "Robot 1 was upgraded with RAM."
        self.assertEqual(expected, result)
        self.assertEqual(250, self.robot.price)
        self.assertEqual(['RAM'], self.robot.hardware_upgrades)

    def test_upgrade_robot_already_upraded(self):
        self.robot.upgrade("RAM", 100)
        result = self.robot.upgrade("RAM", 100)
        expected = "Robot 1 was not upgraded."
        self.assertEqual(expected, result)
        self.assertEqual(['RAM'], self.robot.hardware_upgrades)

    def test_update_robot(self):
        result = self.robot.update(1.1, 1)
        expected = "Robot 1 was updated to version 1.1."
        self.assertEqual(expected, result)
        self.assertEqual([1.1], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)

    def test_update_robot_with_lower_or_same_version(self):
        self.robot.update(1.1, 1)
        result = self.robot.update(1.1, 1)
        expected = "Robot 1 was not updated."
        self.assertEqual(expected, result)
        self.assertEqual([1.1], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)

    def test_update_robot_with_high_capacity_update(self):
        result = self.robot.update(1.1, 3)
        expected = "Robot 1 was not updated."
        self.assertEqual(expected, result)
        self.assertFalse(self.robot.software_updates)
        self.assertEqual(2, self.robot.available_capacity)

    def test_robot_greater_than_other_robot(self):
        self.robot2 = Robot(2, 'Education', 2, 200)
        result = self.robot2 > self.robot
        expected = 'Robot with ID 2 is more expensive than Robot with ID 1.'
        self.assertEqual(expected, result)

    def test_robot_equal_to_other_robot(self):
        self.robot2 = Robot(2, 'Education', 2, 100)
        result = self.robot2 > self.robot
        expected = 'Robot with ID 2 costs equal to Robot with ID 1.'
        self.assertEqual(expected, result)

    def test_robot_cheaper_than_other_robot(self):
        self.robot2 = Robot(2, 'Education', 2, 50)
        result = self.robot2 > self.robot
        expected = 'Robot with ID 2 is cheaper than Robot with ID 1.'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
