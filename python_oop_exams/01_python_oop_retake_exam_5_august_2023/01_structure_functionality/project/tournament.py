from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    valid_equipment_types = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    valid_team_types = {
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

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.valid_equipment_types:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.valid_equipment_types[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.valid_team_types:
            raise Exception("Invalid team type!")
        if self.capacity <= 0:
            return "Not enough tournament capacity."
        self.teams.append(self.valid_team_types[team_type](team_name, country, advantage))
        self.capacity -= 1
        return f"{team_type} was successfully added."

    def get_team_by_name(self, team_name) -> BaseTeam:
        for team in self.teams:
            if team.name == team_name:
                return team

    def get_equipment_by_type(self, equipment_type):
        return [e for e in self.equipment if isinstance(e, self.valid_equipment_types[equipment_type])][-1]

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.get_team_by_name(team_name)
        equipment = self.get_equipment_by_type(equipment_type)
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")
        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.get_team_by_name(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        self.capacity += 1
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for e in self.equipment:
            if isinstance(e, self.valid_equipment_types[equipment_type]):
                e.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self.get_team_by_name(team_name1)
        team2 = self.get_team_by_name(team_name2)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + team1.avg_team_protection
        team2_points = team2.advantage + team2.avg_team_protection

        if team1_points == team2_points:
            return "No winner in this game."

        winner = team1 if team1_points > team2_points else team2

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda x: -x.wins)
        team_statistics = "\n".join([str(t.get_statistics()) for t in teams])
        return (f"Tournament: {self.name}\n"
                f"Number of Teams: {len(self.teams)}\n"
                f"Teams:\n{team_statistics}")
