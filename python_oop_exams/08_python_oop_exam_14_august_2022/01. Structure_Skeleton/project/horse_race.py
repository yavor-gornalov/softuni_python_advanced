from typing import List

from project.jockey import Jockey


class HorseRace:
    AVAILABLE_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: List[Jockey] = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in self.AVAILABLE_RACE_TYPES:
            raise ValueError("Race type does not exist!")
        self.__race_type = value

    @property
    def jockey_registered(self):
        return [x.name for x in self.jockeys]
