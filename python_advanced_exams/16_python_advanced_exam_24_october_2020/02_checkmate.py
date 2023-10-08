KING, QUEEN, EMPTY = "K", "Q", "."
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

size = 8
board = []
attackers = []
king_position = -1, -1
for r in range(size):
    line = input().split()
    if KING in line:
        king_position = r, line.index(KING)
    board.append(line)

for r, c in DIRECTIONS.values():
    row, col = king_position
    row, col = row + r, col + c
    while 0 <= row < size and 0 <= col < size:
        if board[row][col] == QUEEN:
            attackers.append([row, col])
            break
        row, col = row + r, col + c

print(*attackers, sep='\n') if attackers else print("The king is safe!")
