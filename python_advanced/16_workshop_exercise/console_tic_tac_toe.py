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


def setup_board(matrix=None, size=3):
    global first_player
    if not matrix:
        matrix, number = [], 0
        for i in range(size):
            row = []
            for j in range(size):
                number += 1
                row.append(str(number))
            matrix.append(row)
        print("This is numeration of the board:")
        [print(f"|  {'  |  '.join(matrix[i])}  |") for i in range(size)]
        print(f"{first_player.name} starts first!")
    else:
        size = len(matrix)
        for i in range(size):
            row = [matrix[i][j] if not matrix[i][j].isdigit() else ' ' for j in range(size)]
            print(f"|  {'  |  '.join(row)}  |")

    return matrix


def player_move(matrix, player):
    size = len(matrix)
    board_positions, key = {}, 0
    for i in range(size):
        for j in range(size):
            key += 1
            board_positions[key] = (i, j)

    while True:
        try:
            position = int(input(f"{player.name}, choose a free position [1-{size ** 2}]: "))

            if position not in board_positions:
                raise ValueError
            r, c = board_positions[position]

            if matrix[r][c] in "XO":
                raise ValueError
            matrix[r][c] = player.symbol
            break

        except ValueError:
            print("Invalid position!")

    return matrix


# first_player, second_player = get_players()
first_player, second_player = Player("Yavor", "X"), Player("Rally", "O")
board = setup_board(size=3)

while True:
    player_move(board, first_player)
    setup_board(board)

    first_player, second_player = second_player, first_player
