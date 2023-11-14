from project.meals.meal import Meal


class Starter(Meal):
    TYPE = "Starter"

    def __init__(self, name: str, price: float, quantity: int = 60):
        super().__init__(name, price, quantity)

    @property
    def meal_type(self):
        return Starter.TYPE


if __name__ == "__main__":
    s1 = Starter("French toast", 6.50, 5)
    s2 = Starter("Hummus and Avocado Sandwich", 7.90)
    print(s1.quantity)
    print(s2.quantity)
