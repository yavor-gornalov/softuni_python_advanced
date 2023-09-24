from collections import deque

FREE, BUNNY, PLAYER = ".", "B", "P"
DIRECTIONS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

rows, cols = [int(x) for x in input().split()]
row, col = None, None
bunnies = set()
field = []
for r in range(rows):
    line = list(input())
    for c in range(cols):
        if line[c] == PLAYER:
            row, col = r, c
        if line[c] == BUNNY:
            bunnies.add((r, c))
    field.append(line)

commands = deque(input())

end_game = False
player_won = False

while not end_game:
    command = commands.popleft()
    if command not in DIRECTIONS:
        continue
    r, c = DIRECTIONS[command]
    next_r, next_c = row + r, col + c
    if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
        end_game = True
        player_won = True
        field[row][col] = FREE

    elif field[next_r][next_c] == BUNNY:
        end_game = True
        field[row][col] = FREE
        row, col = next_r, next_c
    else:
        field[row][col] = FREE
        field[next_r][next_c] = PLAYER
        row, col = next_r, next_c

    for bunny_position in bunnies.copy():
        for direction in DIRECTIONS.values():
            r, c = direction
            row0, col0 = bunny_position
            next_r, next_c = row0 + r, col0 + c
            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                continue
            if field[next_r][next_c] == PLAYER:
                player_won = False
                end_game = True
            field[next_r][next_c] = BUNNY
            bunnies.add((next_r, next_c))

[print(*line, sep="") for line in field]
if end_game and player_won:
    print(f"won: {row} {col}")
elif end_game and not player_won:
    print(f"dead: {row} {col}")
