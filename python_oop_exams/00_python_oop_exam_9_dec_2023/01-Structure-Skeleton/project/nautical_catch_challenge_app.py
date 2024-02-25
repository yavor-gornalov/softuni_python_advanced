from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.__get_item_by_attr(self.divers, name=diver_name):
            return f"{diver_name} is already a participant -> {diver_type}."

        new_diver = self.DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.__get_item_by_attr(self.fish_list, name=fish_name):
            return f"{fish_name} is already allowed as a {fish_type}."

        new_fish = self.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver: BaseDiver = self.__get_item_by_attr(self.divers, name=diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish: BaseFish = self.__get_item_by_attr(self.fish_list, name=fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        collection = [d for d in self.divers if d.has_health_issue]
        if collection:
            for diver in collection:
                diver.has_health_issue = False
                diver.renew_oxy()

        return f"Divers recovered: {len(collection)}"

    def diver_catch_report(self, diver_name: str):
        diver: BaseDiver = self.__get_item_by_attr(self.divers, name=diver_name)
        result = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            result.append(fish.fish_details())

        return "\n".join(result)

    def competition_statistics(self):
        result = ["**Nautical Catch Challenge Statistics**"]
        for diver in sorted(self.divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name)):
            if diver.has_health_issue:
                continue
            result.append(str(diver))
        return "\n".join(result)

    # HELPERS:
    @staticmethod
    def __get_item_by_attr(collection, **kwargs):
        for attr, value in kwargs.items():
            return next((x for x in collection if getattr(x, attr, None) == value), None)
