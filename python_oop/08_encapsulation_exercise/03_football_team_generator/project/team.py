from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def player_exists(self, player_name: str) -> bool:
        for player in self.__players:
            if player.name == player_name:
                return True
        return False

    def add_player(self, player: Player) -> str:
        if self.player_exists(player.name):
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> [Player, str]:
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"
