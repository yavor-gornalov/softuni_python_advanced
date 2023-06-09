MIN_SIZE, MAX_SIZE = 3, 99
PLAYER = {1: "X", 2: "O"}
EMPTY = "."


def read_settings(low_limit, up_limit, text="Enter a value: "):
    while True:
        try:
            setting = int(input(text))
            if low_limit <= setting <= up_limit:
                break
            raise ValueError
        except ValueError:
            print("Please enter a valid number")
    return setting


def init_playground(rows: int, cols: int):
    field = [[EMPTY for _ in range(cols)] for _ in range(rows)]
    return field


def plot_playground(field, sep="  "):
    rows, cols = len(field), len(field[0])
    print()
    [print(*field[r], sep=sep) for r in range(rows)]
    print()
    # print(*[i for i in range(1, cols + 1)], sep=" " * len(sep))


def player_move(field, player):
    rows, cols = len(field), len(field[0])
    while True:
        try:
            col = int(input(f"Player {player}, please a column: ")) - 1  # index
            if not 0 <= col < cols:
                raise ValueError
        except ValueError:
            print(f"Please input an column number between 1 and {playground_cols}!")
        else:
            break

        # print("Please enter a valid column number!")
    for row in range(rows - 1, -1, -1):
        if field[row][col] == EMPTY:
            field[row][col] = PLAYER[player]
            return row, col
    else:
        print("Please choose another column. This column is full!")


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
        while r >= 0 and c < cols and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r -= 1
            c += 1
        r, c = row, col
        while r < rows and c >= 0 and field[r][c] == PLAYER[player]:
            sequence.add((r, c))
            r += 1
            c -= 1
        return len(sequence)

    if any(x >= winning_sequence for x in
           [check_up_down(), check_left_right(), check_left_diagonal(), check_right_diagonal()]):
        return player


playground_rows = read_settings(MIN_SIZE, MAX_SIZE, f"Enter number of playground rows[{MIN_SIZE}-{MAX_SIZE}]: ")
playground_cols = read_settings(MIN_SIZE, MAX_SIZE, f"Enter number of playground cols[{MIN_SIZE}-{MAX_SIZE}]: ")
winning_sequence = read_settings(
    MIN_SIZE, min(playground_rows, playground_cols),
    f"Enter number of winning sequence[{MIN_SIZE}-{min(playground_rows, playground_cols)}]: ")

playground = init_playground(playground_rows, playground_cols)
plot_playground(playground, sep="  |  ")

current_player, next_player = 1, 2
winner, turn = None, 0
possible_moves = playground_rows * playground_cols
while turn < possible_moves:
    result = player_move(playground, current_player)
    if result:
        plot_playground(playground, sep="  |  ")
        winner = check_winning_combination(playground, current_player, result[0], result[1])
    if winner:
        print(f"Player {current_player} has won this game!")
        break
    current_player, next_player = next_player, current_player
    turn += 1
else:
    print("No winner in this game!")
