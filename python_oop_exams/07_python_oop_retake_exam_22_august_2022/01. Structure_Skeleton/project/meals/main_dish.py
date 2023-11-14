from project.meals.meal import Meal


class MainDish(Meal):
    TYPE = "Main Dish"

    def __init__(self, name: str, price: float, quantity: int = 50):
        super().__init__(name, price, quantity)

    @property
    def meal_type(self):
        return MainDish.TYPE
