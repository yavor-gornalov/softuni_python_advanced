from typing import List

from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Hen(Bird):
    @property
    def preferred_food(self) -> list:
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def weight_index(self) -> float:
        return 0.35

    def make_sound(self):
        return "Cluck"


class Owl(Bird):
    @property
    def preferred_food(self) -> list:
        return [Meat]

    @property
    def weight_index(self) -> float:
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"
