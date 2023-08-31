from project.cat import Cat

from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Tomcat")

    def test_initialized_correctly(self):
        self.assertEqual("Tomcat", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_increase_size_after_eating(self):
        expected_size = 1
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        self.cat.fed = False
        expected_size = 2
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)

    def test_raising_error_after_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        expected_message = 'Already fed.'
        self.assertEqual(expected_message, str(ex.exception))

    def test_raise_error_after_go_to_sleap_hungry(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        expected_message = 'Cannot sleep while hungry'
        self.assertEqual(expected_message, str(ex.exception))

    def test_not_sleepy_after_sleep(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
