PLAYER, EMPTY, VISITED = "Y", ".", "x"
DIRECTIONS = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}
items_collected = {"D": ["Christmas decorations", 0],
                   "G": ["Gifts", 0],
                   "C": ["Cookies", 0]}


def player_move(matrix, pos, direct, stp, items, total):
    row, col = pos
    for _ in range(stp):
        if not total:
            break
        matrix[row][col] = VISITED
        row = (row + DIRECTIONS[direct][0]) % len(matrix)
        col = (col + DIRECTIONS[direct][1]) % len(matrix[0])
        if matrix[row][col] in items:
            items[matrix[row][col]][1] += 1
            total -= 1
        matrix[row][col] = PLAYER
    return (row, col), total


rows, cols = [int(x) for x in input().split(", ")]

field = []
player_position = (None, None)
total_items = 0
for r in range(rows):
    line = input().split()
    for c in range(cols):
        if line[c] == PLAYER:
            player_position = r, c
        if line[c] in items_collected:
            total_items += 1
    field.append(line)

result = []
while total_items:
    line = input()
    if line == "End":
        break
    command = line.split("-")
    direction, step = command[0], int(command[1])
    player_position, total_items = player_move(field, player_position, direction, step, items_collected, total_items)
else:
    result.append("Merry Christmas!")

result.append("You've collected:")
[result.append(f"- {num} {typ}") for (typ, num) in items_collected.values()]
[result.append(" ".join(row)) for row in field]
print("\n".join(result))
