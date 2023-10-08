PLAYER, EMPTY = "P", "-"
DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

initial_string = input()
size = int(input())

field = []
row, col = None, None  # player position
for r in range(size):
    line = [x for x in input()]
    if PLAYER in line:
        row, col = r, line.index(PLAYER)
    field.append(line)

commands_count = int(input())
for _ in range(commands_count):
    command = input()
    if command not in DIRECTIONS:
        continue

    field[row][col] = EMPTY
    next_row = row + DIRECTIONS[command][0]
    next_col = col + DIRECTIONS[command][1]
    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
        initial_string = initial_string[:-1]
        field[row][col] = PLAYER
        continue

    if field[next_row][next_col] != EMPTY:
        initial_string += field[next_row][next_col]
    field[next_row][next_col] = PLAYER
    row, col = next_row, next_col

print(initial_string)
[print(*line, sep="") for line in field]
