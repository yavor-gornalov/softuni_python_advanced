from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def preferred_food(self) -> list:
        return [Vegetable, Fruit]

    @property
    def weight_index(self) -> float:
        return 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def preferred_food(self) -> list:
        return [Meat]

    @property
    def weight_index(self) -> float:
        return 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def preferred_food(self) -> list:
        return [Vegetable, Meat]

    @property
    def weight_index(self) -> float:
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def preferred_food(self) -> list:
        return [Meat]

    @property
    def weight_index(self) -> float:
        return 1.00

    def make_sound(self: Food):
        return "ROAR!!!"
