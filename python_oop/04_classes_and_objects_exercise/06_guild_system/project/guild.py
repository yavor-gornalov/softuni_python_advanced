from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if any([player.name == p.name for p in self.players]):
            return f"Player {player.name} is already in the guild."

        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        current_player = None
        for player in self.players:
            if player.name == player_name:
                current_player = player
                break

        if not current_player:
            return f"Player {player_name} is not in the guild."

        current_player.guild = "Unaffiliated"
        self.players.remove(current_player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()
        return result
