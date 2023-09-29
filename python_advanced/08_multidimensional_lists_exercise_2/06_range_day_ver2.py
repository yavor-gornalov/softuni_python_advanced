AIM, TARGET, EMPTY = "A", "x", "."
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}


def validate_coordinates(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def move_aim(matrix, position, direction, steps):
    row, col = position
    next_row = row + DIRECTIONS[direction][0] * steps
    next_col = col + DIRECTIONS[direction][1] * steps
    if not validate_coordinates(next_row, next_col) or matrix[next_row][next_col] != EMPTY:
        return row, col
    matrix[row][col] = EMPTY
    matrix[next_row][next_col] = AIM
    return next_row, next_col


def shoot(matrix, position, direction):
    r0, c0 = DIRECTIONS[direction]
    row = position[0] + r0
    col = position[1] + c0
    while validate_coordinates(row, col):
        if matrix[row][col] == TARGET:
            matrix[row][col] = EMPTY
            return [row, col]
        row += r0
        col += c0


SIZE = 5

matrix = []
aim_position = (None, None)
targets_count = 0
for r in range(SIZE):
    line = [x for x in input().split()]
    if AIM in line:
        aim_position = r, line.index(AIM)
    if TARGET in line:
        targets_count += line.count(TARGET)
    matrix.append(line)

commands_count = int(input())
target_coordinates = []
for _ in range(commands_count):
    if len(target_coordinates) == targets_count:
        break
    command, direction, *steps = input().split()
    if command == "move":
        aim_position = move_aim(matrix, aim_position, direction, int(steps[0]))
    elif command == "shoot":
        result = shoot(matrix, aim_position, direction)
        target_coordinates.append(result) if result else None

if len(target_coordinates) == targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - len(target_coordinates)} targets left.")
[print(p) for p in target_coordinates]
