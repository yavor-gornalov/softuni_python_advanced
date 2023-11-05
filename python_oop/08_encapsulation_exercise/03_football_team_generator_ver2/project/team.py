from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    @property
    def name(self):
        return self.__name

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        collection = [x for x in self.__players if x.name == player_name]
        if collection:
            player = collection[0]
            self.__players.remove(player)
            return player
        return f"Player {player_name} not found"
