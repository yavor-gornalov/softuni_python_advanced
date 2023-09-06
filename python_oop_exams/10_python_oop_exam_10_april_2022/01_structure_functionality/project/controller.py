from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    SUSTENANCE_TYPES = {
        "Food": Food,
        "Drink": Drink
    }

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        players_currently_added = []
        for player in args:
            if self._get_player_by_name(player.name):
                continue
            self.players.append(player)
            players_currently_added.append(player.name)
        return f"Successfully added: {', '.join(players_currently_added)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.SUSTENANCE_TYPES:
            return

        player = self._get_player_by_name(player_name)
        if player is None:
            return
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        supply_idx = self._get_last_index_of_supply_by_type(sustenance_type)
        if supply_idx is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        supply = self.supplies.pop(supply_idx)
        player.stamina = min(100, player.stamina + supply.energy)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self._get_player_by_name(first_player_name)
        second_player = self._get_player_by_name(second_player_name)

        break_duel_message = self._check_players_for_enough_stamina(first_player, second_player)
        if break_duel_message:
            return '\n'.join(break_duel_message)

        winner = None
        attacker, defender = sorted([first_player, second_player])
        # TODO check damage type
        attacker_damage = attacker.stamina / 2
        defender.stamina = max(0, defender.stamina - attacker_damage)
        if not defender.stamina:
            winner = attacker

        if not winner:
            defender_damage = defender.stamina / 2
            attacker.stamina = max(0, attacker.stamina - defender_damage)

        if not attacker.stamina:
            winner = defender

        if winner is None:
            winner = sorted([attacker, defender])[-1]

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            reduce_value = player.age * 2
            player.stamina = max(0, player.stamina - reduce_value)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        [result.append(str(p)) for p in self.players]
        [result.append(s.details()) for s in self.supplies]
        return '\n'.join(result)

    # helpers
    def _get_player_by_name(self, player_name):
        collection = [p for p in self.players if p.name == player_name]
        return collection[0] if collection else None

    def _get_last_index_of_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, - 1, -1):
            if self.supplies[idx].__class__.__name__ == sustenance_type:
                return idx

    @staticmethod
    def _check_players_for_enough_stamina(*args):
        message = []
        for player in args:
            if player.stamina == 0:
                message.append(f"Player {player.name} does not have enough stamina.")
        return message
