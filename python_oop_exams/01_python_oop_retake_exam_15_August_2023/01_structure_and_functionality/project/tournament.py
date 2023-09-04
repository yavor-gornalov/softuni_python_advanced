from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def _get_team_by_name(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team

    def _get_equipment_by_type(self, equipment_type):
        result = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        return result[-1] if result else None

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.VALID_EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self._get_team_by_name(team_name)
        equipment = self._get_equipment_by_type(equipment_type)
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")
        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._get_team_by_name(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_team_by_name(team_name1)
        team2 = self._get_team_by_name(team_name2)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + team1._total_team_protection
        team2_points = team2.advantage + team2._total_team_protection

        if team1_points == team2_points:
            return "No winner in this game."

        winner = team1 if team1_points > team2_points else team2

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda x: -x.wins)
        result = f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""
        for t in teams:
            result += f"\n{t.get_statistics()}"
        return result
