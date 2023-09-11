from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIANS:
            raise ValueError("Invalid musician type!")
        if self.__get_musician_by_name(name, self.musicians):
            raise Exception(f"{name} is already a musician!")
        new_musician = self.MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.__get_band_by_name(name):
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__get_concert_by_place(place)
        if concert:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__get_musician_by_name(musician_name, self.musicians)
        band = self.__get_band_by_name(band_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = self.__get_musician_by_name(musician_name, band.members)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__get_band_by_name(band_name)
        concert = self.__get_concert_by_place(concert_place)

        if not self.__check_band_members_types(band):
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")
        if not self.__check_band_members_for_needed_skills(band, concert.genre):
            raise Exception(f"The {band.name} band is not ready to play at the concert!")
        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

        # HELPERS

    @staticmethod
    def __get_musician_by_name(musician_name, collection):
        result = [m for m in collection if m.name == musician_name]
        return result[0] if result else None

    def __get_band_by_name(self, band_name):
        collection = [b for b in self.bands if b.name == band_name]
        return collection[0] if collection else None

    def __get_concert_by_place(self, place):
        collection = [c for c in self.concerts if c.place == place]
        return collection[0] if collection else None

    def __check_band_members_types(self, band: Band):
        band_musicians_types = set([m.TYPE_ for m in band.members])
        return len(band_musicians_types) == len(self.MUSICIANS)

    @staticmethod
    def __check_band_members_for_needed_skills(band: Band, concert_type):
        skills_required = {"Rock": {"Drummer": ["play the drums with drumsticks"],
                                    "Singer": ["sing high pitch notes"],
                                    "Guitarist": ["play rock"]},
                           "Metal": {"Drummer": ["play the drums with drumsticks"],
                                     "Singer": ["sing low pitch notes"],
                                     "Guitarist": ["play metal"]},
                           "Jazz": {"Drummer": ["play the drums with drum brushes"],
                                    "Singer": ["sing high pitch notes", "sing low pitch notes"],
                                    "Guitarist": ["play jazz"]}}
        for member_type, needed_skills in skills_required[concert_type].items():
            collection = [m for m in band.members if
                          m.TYPE_ == member_type and all([s in m.skills for s in needed_skills])]
            count_of_members_with_needed_skills = len(collection)
            count_of_all_members_from_current_type = len([m for m in band.members if m.TYPE_ == member_type])
            if count_of_all_members_from_current_type != count_of_members_with_needed_skills:
                return False
        return True
