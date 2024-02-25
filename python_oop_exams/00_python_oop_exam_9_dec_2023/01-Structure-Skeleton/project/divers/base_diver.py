from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    TYPE = "BaseDiver"
    INITIAL_OXYGEN = 1000

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    @abstractmethod
    def reduce_oxygen_percentage(self):
        pass

    def miss(self, time_to_catch: int):
        reduced_time = round(time_to_catch * self.reduce_oxygen_percentage)

        if self.oxygen_level < reduced_time:
            self.oxygen_level = 0
            self.has_health_issue = True

        self.oxygen_level = max(self.oxygen_level - reduced_time, 0)
        if self.oxygen_level <= 0:
            self.has_health_issue = True

    @property
    @abstractmethod
    def initial_oxygen(self):
        pass

    def renew_oxy(self):
        self.oxygen_level = self.initial_oxygen

    @property
    @abstractmethod
    def diver_type(self):
        pass

    def hit(self, fish: BaseFish):
        if fish.time_to_catch > self.oxygen_level:
            self.oxygen_level = 0
            self.has_health_issue = True
            return

        self.catch.append(fish)
        self.oxygen_level -= fish.time_to_catch
        if self.oxygen_level <= 0:
            self.has_health_issue = True
        self.competition_points += round(fish.points, 1)

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        # TODO check formatting needed
        return (f"{self.diver_type}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]")
