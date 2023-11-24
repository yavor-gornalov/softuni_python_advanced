from project.pet_shop import PetShop

from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("My Pet Shop")

    def test_constructor(self):
        self.pet_shop = PetShop("My Pet Shop")
        self.assertEqual("My Pet Shop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_neg_quantity_raises_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("milk", 0)
        expected = "Quantity cannot be equal to or less than 0"
        self.assertEqual(expected, str(ve.exception))

    def test_add_non_existing_food(self):
        result = self.pet_shop.add_food("milk", 450)
        expected = "Successfully added 450.00 grams of milk."
        self.assertEqual(expected, result)
        self.assertEqual({"milk": 450}, self.pet_shop.food)

    def test_add_existing_food(self):
        self.pet_shop.add_food("milk", 450)
        result = self.pet_shop.add_food("milk", 550)
        expected = "Successfully added 550.00 grams of milk."
        self.assertEqual(expected, result)
        self.assertEqual({"milk": 1000}, self.pet_shop.food)

    def test_add_pet(self):
        result = self.pet_shop.add_pet("Tom")
        expected = "Successfully added Tom."
        self.assertEqual(expected, result)
        self.assertEqual(["Tom"], self.pet_shop.pets)

    def test_add_pet_with_existing_name(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_pet("Jerry")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Tom")
        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(["Tom", "Jerry"], self.pet_shop.pets)

    def test_feed_unknown_pet_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("milk", "Tom")
        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_with_unknown_food(self):
        self.pet_shop.add_pet("Tom")
        result = self.pet_shop.feed_pet("milk", "Tom")
        expected = "You do not have milk"
        self.assertEqual(expected, result)

    def test_feed_pet_with_low_food_quantity(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_food("milk", 99)
        result = self.pet_shop.feed_pet("milk", "Tom")
        expected = "Adding food..."
        self.assertEqual(expected, result)
        self.assertEqual(1099, self.pet_shop.food["milk"])

    def test_feed_pet_happy_path(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_food("milk", 100)
        result = self.pet_shop.feed_pet("milk", "Tom")
        expected = "Tom was successfully fed"
        self.assertEqual(expected, result)
        self.assertEqual(0, self.pet_shop.food["milk"])

    def test_representation(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_pet("Jerry")
        self.pet_shop.add_pet("Sparky")
        expected = "Shop My Pet Shop:\nPets: Tom, Jerry, Sparky"
        self.assertEqual(expected, str(self.pet_shop))

    def test_representation_with_no_pets(self):
        expected = "Shop My Pet Shop:\nPets: "
        self.assertEqual(expected, str(self.pet_shop))


if __name__ == "__main__":
    main()
