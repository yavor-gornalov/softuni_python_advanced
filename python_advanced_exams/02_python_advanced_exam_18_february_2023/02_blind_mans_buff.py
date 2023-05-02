# https://judge.softuni.org/Contests/Practice/Index/3889#1

BLIND, PLAYER, OBSTACLE, FREE = "B", "P", "O", "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n, m = [int(x) for x in input().split()]

blind_position = None
field = []
for r in range(n):
    line = input().split()
    if BLIND in line:
        blind_position = [r, line.index(BLIND)]
    field.append(line)

touched_players, moves = 0, 0
while True:
    command = input()
    if command == "Finish":
        break
    if touched_players == 3:
        break

    r0, c0 = blind_position
    row = r0 + directions[command][0]
    col = c0 + directions[command][1]

    if not (0 <= row < n and 0 <= col < m) or field[row][col] == OBSTACLE:
        continue

    if field[row][col] == PLAYER:
        touched_players += 1

    field[r0][c0] = FREE
    field[row][col] = BLIND
    blind_position = [row, col]
    moves += 1

print(f"Game over!\nTouched opponents: {touched_players} Moves made: {moves}")
