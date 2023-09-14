# https://judge.softuni.org/Contests/Practice/Index/4089#1

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}


def is_next_position_valid(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return False
    if col < 0 or col >= len(matrix[0]):
        return False
    return True


rows, cols = [int(x) for x in input().split()]

start_position = None
field = []
for row in range(rows):
    line = input()
    if "B" in line:
        start_position = [row, line.index("B")]
    field.append(list(line))

current_position = start_position

finished = False
while not finished:
    command = input()
    if command not in directions:
        continue
    r, c = directions[command]
    next_r = current_position[0] + r
    next_c = current_position[1] + c

    if not is_next_position_valid(field, next_r, next_c):
        start_r, start_c = start_position
        field[start_r][start_c] = " "
        print("The delivery is late. Order is canceled.")
        finished = True

    elif field[next_r][next_c] == "A":
        field[next_r][next_c] = "P"
        print("Pizza is delivered on time! Next order...")
        finished = True

    elif field[next_r][next_c] == "*":
        continue

    elif field[next_r][next_c] == "P":
        field[next_r][next_c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    if field[current_position[0]][current_position[1]] == "-":
        field[current_position[0]][current_position[1]] = "."
    current_position = [next_r, next_c]

[print(*field[row], sep="") for row in range(len(field))]
