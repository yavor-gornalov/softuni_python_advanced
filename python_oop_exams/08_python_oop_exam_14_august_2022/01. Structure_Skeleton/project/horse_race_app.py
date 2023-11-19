from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    AVAILABLE_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @property
    def race_types_created(self):
        return [x.race_type for x in self.horse_races]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.__get_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in self.AVAILABLE_HORSE_TYPES:
            new_horse = self.AVAILABLE_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__get_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.race_types_created:
            raise f"Race {race_type} has been already created!"

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__get_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.__get_last_horse_of_type(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__get_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey_name in horse_race.jockey_registered:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockey_registered) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self.__get_race_winner(horse_race)
        return (f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! "
                f"Winner's horse: {winner.horse.name}.")

    # HELPERS:
    def __get_horse_by_name(self, horse_name):
        return next((x for x in self.horses if x.name == horse_name), None)

    def __get_jockey_by_name(self, jokey_name):
        return next((x for x in self.jockeys if x.name == jokey_name), None)

    def __get_horse_race_by_type(self, race_type):
        return next((x for x in self.horse_races if x.race_type == race_type), None)

    def __get_last_horse_of_type(self, horse_type):
        horse = None
        for current_horse in self.horses:
            if current_horse.__class__.__name__ == horse_type and not current_horse.is_taken:
                horse = current_horse
        return horse

    @staticmethod
    def __get_race_winner(horse_race):
        winner = None
        winning_speed = 0
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > winning_speed:
                winner = jockey
                winning_speed = jockey.horse.speed
        return winner
