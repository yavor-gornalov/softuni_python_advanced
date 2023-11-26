from project.factory.paint_factory import PaintFactory

from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("My Paint Factory", 5)

    def test_constructor(self):
        self.assertEqual("My Paint Factory", self.paint_factory.name)
        self.assertEqual(5, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual({}, self.paint_factory.products)

    def test_can_add_returns_True_there_is_enough_space_for_ingredients(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(True, self.paint_factory.can_add(4))

    def test_can_add_returns_False_not_enough_space_available(self):
        self.paint_factory.ingredients = {"ingredient_1": 1, "ingredient_2": 1}
        self.assertEqual(False, self.paint_factory.can_add(4))

    def test_add_not_valid_ingredient_raises_te(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("purple", 3)
        expected = "Ingredient of type purple not allowed in PaintFactory"
        self.assertEqual(expected, str(te.exception))

    def test_add_ingredient_quantity_over_the_limit_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("white", 6)
        expected = "Not enough space in factory"
        self.assertEqual(expected, str(ve.exception))

    def test_add_ingredient_for_first_time(self):
        self.paint_factory.add_ingredient("blue", 3)
        self.assertEqual({"blue": 3}, self.paint_factory.products)

    def test_add_ingredient_add_quantity_to_existing_ingredient(self):
        self.paint_factory.add_ingredient("blue", 2)
        self.paint_factory.add_ingredient("red", 1)
        self.paint_factory.add_ingredient("blue", 1)
        self.paint_factory.add_ingredient("red", 1)
        self.assertEqual({"blue": 3, "red": 2}, self.paint_factory.products)

    def test_remove_non_existing_ingredient_raises_ke(self):
        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("blue", 2)
        expected = "'No such ingredient in the factory'"
        self.assertEqual(expected, str(ke.exception))

    def test_remove_ingredient_above_existing_quantity_raises_ve(self):
        self.paint_factory.add_ingredient("blue", 2)
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("blue", 3)
        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_ingredient_below_or_equal_to_existing_quantity(self):
        self.paint_factory.ingredients = {"blue": 3, "red": 2}
        self.paint_factory.remove_ingredient("blue", 2)
        self.assertEqual({"blue": 1, "red": 2}, self.paint_factory.products)
        self.paint_factory.remove_ingredient("red", 2)
        self.assertEqual({"blue": 1, "red": 0}, self.paint_factory.products)

    def test_repr_dunder(self):
        self.paint_factory.ingredients = {"blue": 3, "red": 2}
        result = str(self.paint_factory)
        expected = (f"Factory name: My Paint Factory with capacity 5.\n"
                    f"blue: 3\n"
                    f"red: 2\n")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
