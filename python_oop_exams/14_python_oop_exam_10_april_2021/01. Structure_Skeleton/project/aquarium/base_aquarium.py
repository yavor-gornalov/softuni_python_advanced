from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    FISH_TYPES = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, new_fish: BaseFish):
        if self.fish_type != new_fish.fish_type:
            return "Water not suitable."

        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(new_fish)
        return f"Successfully added {new_fish.fish_type} to {self.name}."

    def remove_fish(self, fish_to_remove: BaseFish):
        if fish_to_remove not in self.fish:
            return
        self.fish.remove(fish_to_remove)

    def add_decoration(self, new_decoration: BaseDecoration):
        self.decorations.append(new_decoration)

    def feed(self):
        [f.eat() for f in self.fish]
        return f"Fish fed: {len(self.fish)}"

    @property
    def value(self):
        return sum([f.price for f in self.fish]) + sum([d.price for d in self.decorations])

    def __str__(self):
        fish_collection = " ".join([f.name for f in self.fish]) if self.fish else "none"
        return f"""{self.name}:
Fish: {fish_collection}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}"""
