ROWS, COLS = 6, 7
PLAYER = {1: "@", 2: "#"}
EMPTY = "-"


def init_playground(rows: int, cols: int):
    field = [[EMPTY for _ in range(cols)] for _ in range(rows)]
    return field


def plot_playground(field):
    rows = len(field)
    [print(*field[r], sep=" ") for r in range(rows)]
    print()


def player_move(field, player):
    rows, cols = len(field), len(field[0])
    col = int(input(f"Player {player}, please a column: ")) - 1  # index
    for row in range(rows - 1, -1, -1):
        if field[row][col] == EMPTY:
            field[row][col] = PLAYER[player]
            return row, col
    else:
        print("This column is full!")


playground = init_playground(ROWS, COLS)
plot_playground(playground)

current_player, next_player = 1, 2
while True:
    player_move(playground, current_player)
    plot_playground(playground)

    current_player, next_player = next_player, current_player
