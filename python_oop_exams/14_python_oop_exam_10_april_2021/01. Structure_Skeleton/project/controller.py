from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    AQUARIUM_TYPES = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    DECORATION_TYPES = {"Ornament": Ornament, "Plant": Plant}
    FISH_TYPES = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.AQUARIUM_TYPES:
            return "Invalid aquarium type."

        new_aquarium = self.AQUARIUM_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.DECORATION_TYPES:
            return "Invalid decoration type."

        new_decoration = self.DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return

        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return

        new_fish = self.FISH_TYPES[fish_type](fish_name, fish_species, price)
        return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return

        return aquarium.feed()

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return
        return f"The value of Aquarium {aquarium.name} is {aquarium.value:.2f}."

    def report(self):
        result = []
        [result.append(str(a)) for a in self.aquariums]
        return "\n".join(result)

    # HELPERS:
    def __find_aquarium_by_name(self, aquarium_name):
        return next((x for x in self.aquariums if x.name == aquarium_name), None)
