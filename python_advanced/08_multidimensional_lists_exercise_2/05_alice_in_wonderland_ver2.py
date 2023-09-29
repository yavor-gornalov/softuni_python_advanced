ALICE, RABBIT_HOLE, EMPTY, VISITED = "A", "R", ".", "*"
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

size = int(input())

wonderland = []
row, col = None, None  # Alice position (start position)
for r in range(size):
    line = [x for x in input().split()]
    if ALICE in line:
        row, col = r, line.index(ALICE)
        line[col] = VISITED
    wonderland.append(line)

tea_collected = 0
while tea_collected < 10:
    command = input()
    r0, c0 = DIRECTIONS[command]
    next_r = row + r0
    next_c = col + c0

    if next_r < 0 or next_c < 0 or next_r >= size or next_c >= size:
        break
    elif wonderland[next_r][next_c] == RABBIT_HOLE:
        wonderland[next_r][next_c] = VISITED
        break

    if wonderland[next_r][next_c].isnumeric():
        tea_collected += int(wonderland[next_r][next_c])
    wonderland[next_r][next_c] = VISITED
    row, col = next_r, next_c

if tea_collected < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")
[print(*row) for row in wonderland]
