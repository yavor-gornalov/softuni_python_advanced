BUNNY, TRAP = "B", "X"
DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
bunny_position = None
matrix = []
for r in range(size):
    line = list(input().split())
    if BUNNY in line:
        bunny_position = r, line.index(BUNNY)
    matrix.append(line)

max_direction = None
max_egg_sequence = None
max_eggs_collected = 0
for direction, (r, c) in DIRECTIONS.items():
    current_eggs_counter = 0
    current_egg_sequence = []
    row = bunny_position[0] + r
    col = bunny_position[1] + c
    while 0 <= row < size and 0 <= col < size and matrix[row][col] != TRAP:
        eggs_value = int(matrix[row][col])
        if eggs_value > 0:
            current_eggs_counter += eggs_value
            current_egg_sequence.append([row, col])
        row += r
        col += c

    if current_eggs_counter > max_eggs_collected:
        max_eggs_collected = current_eggs_counter
        max_direction = direction
        max_egg_sequence = current_egg_sequence

print(max_direction)
[print(pos) for pos in max_egg_sequence]
print(max_eggs_collected)