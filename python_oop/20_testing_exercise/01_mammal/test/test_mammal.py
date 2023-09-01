from project.mammal import Mammal

from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Tom", "cat", "shsh")

    def test_constructor(self):
        self.assertEqual("Tom", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("shsh", self.mammal.sound)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        expected = "Tom is of type cat"
        self.assertEqual(expected, self.mammal.info())

    def test_make_sound(self):
        expected = "Tom makes shsh"
        self.assertEqual(expected, self.mammal.make_sound())


if __name__ == "__main__":
    main()
