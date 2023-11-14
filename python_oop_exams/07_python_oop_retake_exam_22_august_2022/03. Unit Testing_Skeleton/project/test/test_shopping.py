from project.shopping_cart import ShoppingCart

from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Test', 1000)

    def test_constructor(self):
        self.assertEqual("Test", self.shopping_cart.shop_name)
        self.assertEqual(1000, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_name_setter_without_capital(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'tsst'
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(self.shopping_cart.shop_name, 'Test')

    def test_name_setter_with_number(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'Test1'
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(self.shopping_cart.shop_name, 'Test')

    def test_add_to_cart_expensive_product(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('product', 101)
        expected = "Product product cost too much!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({}, self.shopping_cart.products)

    def test_add_to_cart_product_price_equal_to_100(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('product', 100)
        expected = "Product product cost too much!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({}, self.shopping_cart.products)

    def test_add_product_to_cart_successfully(self):
        expected = "Product product was successfully added to the cart!"
        result = self.shopping_cart.add_to_cart("Product", 99.99)
        self.assertEqual(expected, result)
        self.assertEqual({"Product": 99.99}, self.shopping_cart.products)

    def test_add_duplicate_product_to_cart(self):
        expected = "Bear product was successfully added to the cart!"
        result = self.shopping_cart.add_to_cart("Bear", 99.99)
        self.assertEqual(expected, result)
        self.assertEqual({"Bear": 99.99}, self.shopping_cart.products)
        expected = "Bear product was successfully added to the cart!"
        result = self.shopping_cart.add_to_cart("Bear", 10)
        self.assertEqual(expected, result)
        self.assertEqual({"Bear": 10}, self.shopping_cart.products)

    def test_remove_not_existing_product_from_cart(self):
        self.shopping_cart.add_to_cart("Bear", 10)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Doll")
        expected = "No product with name Doll in the cart!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'Bear': 10}, self.shopping_cart.products)

    def test_remove_existing_product(self):
        self.shopping_cart.add_to_cart("Bear", 10)
        self.shopping_cart.add_to_cart("Doll", 20)
        result = self.shopping_cart.remove_from_cart("Doll")
        expected = "Product Doll was successfully removed from the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({'Bear': 10}, self.shopping_cart.products)

    def test_add_carts(self):
        c1 = ShoppingCart("First", 10)
        c2 = ShoppingCart("Second", 20)
        c1.add_to_cart("Bear", 10)
        c2.add_to_cart("Doll", 20)
        c3 = c1 + c2
        self.assertEqual("FirstSecond", c3.shop_name)
        self.assertEqual(30, c3.budget)
        self.assertEqual({"Bear": 10, "Doll": 20}, c3.products)
        self.assertEqual(True, isinstance(c3, ShoppingCart))

    def test_adding_carts_failure(self):
        a = "ShoppingCart"
        expected = "'str' object has no attribute 'shop_name'"
        with self.assertRaises(AttributeError) as ae:
            self.shopping_cart.__add__(a)
        self.assertEqual(expected, str(ae.exception))

    def test_buy_products_over_budget(self):
        self.shopping_cart.budget = 10
        self.shopping_cart.add_to_cart("Bear", 10)
        self.shopping_cart.add_to_cart("Doll", 20)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        expected = "Not enough money to buy the products! Over budget with 20.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products(self):
        self.shopping_cart.budget = 30
        self.shopping_cart.add_to_cart("Bear", 10)
        self.shopping_cart.add_to_cart("Doll", 20)
        expected = "Products were successfully bought! Total cost: 30.00lv."
        self.assertEqual(expected, self.shopping_cart.buy_products())


if __name__ == "__main__":
    main()
