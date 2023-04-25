class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


def get_players():
    while True:
        invalid_player_name = "Player name should be at least 1 character!"
        first_player_name = input("Enter first player name: ")
        if len(first_player_name) > 0:
            break
        print(invalid_player_name)
    while True:
        second_player_name = input("Enter second player name: ")
        if len(second_player_name) > 0:
            break
        print(invalid_player_name)

    while True:
        first_player_symbol = input("Choose symbol X or O for first player: ").upper()
        if first_player_symbol in "XO":
            break

    second_player_symbol = "O" if first_player_symbol == "X" else "X"

    return Player(first_player_name, first_player_symbol), Player(second_player_name, second_player_symbol)


first_player, second_player = get_players()
