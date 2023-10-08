BOMB = "*"
DIRECTIONS = {
    "up": (-1, 0),
    "up-right": (-1, 1),
    "right": (0, 1),
    "down-right": (1, 1),
    "down": (1, 0),
    "down-left": (1, -1),
    "left": (0, -1),
    "up-left": (-1, -1)
}

size = int(input())
number_of_bombs = int(input())
field = [[""] * size for _ in range(size)]
bombs = [[int(x) for x in input()[1:-1].split(', ')] for _ in range(number_of_bombs)]

for r, c in bombs:
    field[r][c] = BOMB

for row in range(size):
    for col in range(size):
        if field[row][col] == BOMB:
            continue
        current_bombs_count = 0
        for r, c in DIRECTIONS.values():
            next_r, next_c = row + r, col + c
            if next_r < 0 or next_c < 0 or next_r >= size or next_c >= size:
                continue
            current_bombs_count += field[next_r][next_c] == BOMB
        field[row][col] = str(current_bombs_count)

[print(*row) for row in field]
