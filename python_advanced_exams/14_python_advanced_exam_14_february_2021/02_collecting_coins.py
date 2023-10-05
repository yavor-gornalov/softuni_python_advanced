PLAYER, WALL, VISITED = "P", "X", "V"

DIRECTIONS = {
    "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)
}

size = int(input())
matrix = []
player_position = [None, None]
for r in range(size):
    line = input().split()
    if PLAYER in line:
        player_position = [r, line.index(PLAYER)]
    matrix.append(line)

collected_coins = 0
path = [player_position]
result = []
while collected_coins < 100:
    row, col = player_position
    matrix[row][col] = VISITED

    command = input()
    if command not in DIRECTIONS:
        continue

    row = (row + DIRECTIONS[command][0]) % size
    col = (col + DIRECTIONS[command][1]) % size
    path.append([row, col])

    if matrix[row][col] == WALL:
        collected_coins //= 2
        result.append(f"Game over! You've collected {collected_coins} coins.")
        break

    if matrix[row][col] != VISITED:
        collected_coins += int(matrix[row][col])
    player_position = row, col
else:
    result.append(f"You won! You've collected {collected_coins} coins.")

result.append("Your path:")
[result.append(str(x)) for x in path]

print('\n'.join(result))
