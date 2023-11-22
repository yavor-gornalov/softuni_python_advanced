from abc import ABC, abstractmethod


class Astronaut(ABC):
    UNITS_PER_BREATHE = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @property
    @abstractmethod
    def units_per_breathe(self):
        pass

    def breathe(self):
        self.oxygen -= self.UNITS_PER_BREATHE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def collect_item(self, item):
        self.backpack.append(item)

    def __gt__(self, other):
        return self.oxygen > other.oxygen

    def __str__(self):
        return f"""Name: {self.name}
Oxygen: {self.oxygen}
Backpack items: {', '.join([i for i in self.backpack]) if self.backpack else "none"}"""
