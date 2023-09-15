# https://judge.softuni.org/Contests/Practice/Index/4081#1

MOUSE = "M"
CHEESE = "C"
EMPTY = "*"
WALL = "@"
TRAP = "T"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

rows, cols = [int(x) for x in input().split(",")]

field = []
pieces_of_cheese = 0
mouse_position = None
for r in range(rows):
    line = list(input())
    if MOUSE in line:
        mouse_position = [r, line.index(MOUSE)]
    if CHEESE in line:
        pieces_of_cheese += line.count(CHEESE)
    field.append(line)

result = []
while True:
    command = input()
    if command == "danger":
        result.append("Mouse will come back later!")
        break
    if command not in directions:
        continue

    prev_r, prev_c = mouse_position
    r, c = directions[command]
    row, col = prev_r + r, prev_c + c

    if not 0 <= row <= len(field) or not 0 <= col < len(field[0]):
        field[prev_r][prev_c] = MOUSE
        result.append("No more cheese for tonight!")
        break

    elif field[row][col] == CHEESE:
        pieces_of_cheese -= 1
        field[prev_r][prev_c] = EMPTY
        field[row][col] = MOUSE
        if not pieces_of_cheese:
            result.append("Happy mouse! All the cheese is eaten, good night!")
            break
    elif field[row][col] == TRAP:
        field[prev_r][prev_c] = EMPTY
        field[row][col] = MOUSE
        result.append("Mouse is trapped!")
        break
    elif field[row][col] == WALL:
        continue

    field[prev_r][prev_c] = EMPTY
    mouse_position = [row, col]

[result.append(''.join(row)) for row in field]
print("\n".join(result))
