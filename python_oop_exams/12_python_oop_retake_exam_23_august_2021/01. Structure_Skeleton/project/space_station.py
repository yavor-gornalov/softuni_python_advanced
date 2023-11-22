from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        new_astronaut = self.ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.attach_items(items)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = self.__get_top_5_astronauts()
        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        # mission
        explorers_count = 0
        while astronauts:
            current_astronaut = astronauts.pop(0)
            explorers_count += 1

            while planet.items and current_astronaut.oxygen > 0:
                item = planet.items.pop()
                current_astronaut.collect_item(item)
                current_astronaut.breathe()

            if not planet.items:
                break

        if planet.items:
            self.failed_missions += 1
            return "Mission is not completed."

        self.successful_missions += 1
        return f"Planet: {planet.name} was explored. {explorers_count} astronauts participated in collecting items."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.failed_missions} missions were not completed!",
                  "Astronauts' info:"]
        [result.append(str(x)) for x in self.astronaut_repository.astronauts]
        return '\n'.join(result)

    # HELPERS:
    def __get_top_5_astronauts(self):
        collection = [a for a in self.astronaut_repository.astronauts if a.oxygen >= 30]
        if collection:
            return sorted(collection, reverse=True)[:5]
