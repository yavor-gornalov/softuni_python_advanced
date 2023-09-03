from abc import ABC, abstractmethod
from typing import List
from math import floor

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: str):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @property
    def total_price_of_team_equipment(self):
        return sum([e.price for e in self.equipment])

    @property
    def avg_team_protection(self):
        return sum([e.protection for e in self.equipment])

    @property
    @abstractmethod
    def winning_points(self):
        pass

    def win(self):
        self.advantage += self.winning_points
        self.wins += 1

    def get_statistics(self):
        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {self.total_price_of_team_equipment:.2f}\n"
                f"Average Protection: {floor(self.avg_team_protection)}")
