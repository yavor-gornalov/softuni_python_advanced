# https://judge.softuni.org/Contests/Practice/Index/3515#1

class Player:
    def __init__(self, name, is_skipped):
        self.name = name
        self.is_skipped = is_skipped


FIELD_SIZE = 6
EXIT, TRAP, WALL, EMPTY = "E", "T", "W", "."

player_names = input().split(", ")

current_player = Player(player_names[0], False)
next_player = Player(player_names[1], False)

field = [input().split() for _ in range(FIELD_SIZE)]

while True:
    row, col = [int(x) for x in input() if x.isnumeric()]

    if current_player.is_skipped:
        current_player.is_skipped = False
        current_player, next_player = next_player, current_player
        continue

    if field[row][col] == EXIT:
        print(f"{current_player.name} found the Exit and wins the game!")
        break
    elif field[row][col] == TRAP:
        print(f"{current_player.name} is out of the game! The winner is {next_player.name}.")
        break
    elif field[row][col] == WALL:
        print(f"{current_player.name} hits a wall and needs to rest.")
        current_player.is_skipped = True

    current_player, next_player = next_player, current_player
