ROWS, COLS = 6, 7
PLAYER = {1: "@", 2: "#"}
EMPTY = "-"
WINNING_SEQUENCE = 3


def init_playground(rows: int, cols: int):
    field = [[EMPTY for _ in range(cols)] for _ in range(rows)]
    return field


def plot_playground(field):
    rows = len(field)
    [print(*field[r], sep=" ") for r in range(rows)]
    print()


def player_move(field, player):
    rows, cols = len(field), len(field[0])
    while True:
        col = int(input(f"Player {player}, please a column: ")) - 1  # index
        if 0 <= col < cols:
            break
        print("Please enter a valid column number!")
    for row in range(rows - 1, -1, -1):
        if field[row][col] == EMPTY:
            field[row][col] = PLAYER[player]
            return row, col
    else:
        print("This column is full!")


def check_winning_combination(field, player, row, col):
    rows, cols = len(field), len(field[0])

    def check_up_down():
        sequence = set()
        r, c = row, col
        while r >= 0 and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r -= 1
        r, c = row, col
        while r < rows and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r += 1
        return len(sequence)

    def check_left_right():
        sequence = set()
        r, c = row, col
        while c >= 0 and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            c -= 1
        r, c = row, col
        while c < cols and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            c += 1
        return len(sequence)

    def check_left_diagonal():
        sequence = set()
        r, c = row, col
        while r >= 0 and c >= 0 and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r -= 1
            c -= 1
        r, c = row, col
        while r < rows and c < cols and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r += 1
            c += 1
        return len(sequence)

    def check_right_diagonal():
        sequence = set()
        r, c = row, col
        while r >= 0 and c >= 0 and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r -= 1
            c += 1
        r, c = row, col
        while r < rows and c < cols and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r += 1
            c -= 1
        return len(sequence)

    if any([
        check_up_down() >= WINNING_SEQUENCE,
        check_left_right() >= WINNING_SEQUENCE,
        check_left_diagonal() >= WINNING_SEQUENCE,
        check_right_diagonal() >= WINNING_SEQUENCE,
    ]):
        return player


playground = init_playground(ROWS, COLS)
plot_playground(playground)

current_player, next_player = 1, 2
winner = None
while True:
    result = player_move(playground, current_player)
    if result:
        plot_playground(playground)
        winner = check_winning_combination(playground, current_player, result[0], result[1])
    if winner:
        print(f"Player {current_player} has won this game!")
        break

    current_player, next_player = next_player, current_player
