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
    global current_player
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
        print(f"{current_player.name} starts first!")
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
                print("This field is already occupied!")
                continue
            matrix[r][c] = player.symbol
            break

        except ValueError:
            print("Invalid position!")

    return matrix


def check_winner(matrix, player):
    size = len(matrix)

    row_winner = False
    for i in range(size):
        if all([symbol == player.symbol for symbol in matrix[i]]):
            row_winner = True
            break

    col_winner = False
    for j in range(size):
        col = []
        for i in range(size):
            col.append(matrix[i][j])
        if all([symbol == player.symbol for symbol in col]):
            col_winner = True
            break

    diagonal_winner = False
    left_diagonal = [matrix[i][i] for i in range(size)]
    right_diagonal = [matrix[i][size - i - 1] for i in range(size)]

    for diagonal in left_diagonal, right_diagonal:
        if all([symbol == player.symbol for symbol in diagonal]):
            diagonal_winner = True
            break

    if any([row_winner, col_winner, diagonal_winner]):
        print(f"{player.name} has won this game!")
        return True

    return False


BOARD_SIZE = 3

current_player, second_player = get_players()
# first_player, second_player = Player("First", "X"), Player("Second", "O")
board = setup_board(size=BOARD_SIZE)

possible_moves = BOARD_SIZE ** 2
while possible_moves:
    player_move(board, current_player)
    setup_board(board)
    if check_winner(board, current_player):
        break
    current_player, second_player = second_player, current_player
    possible_moves -= 1
else:
    print("No winner in this game!")
