# https://judge.softuni.org/Contests/Practice/Index/3534#1

SIZE = 6
EMPTY_CELL = "."

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def create(mtrx, *args):
    pos, val = args
    if mtrx[pos[0]][pos[1]] == EMPTY_CELL:
        mtrx[pos[0]][pos[1]] = val[0]


def update(mtrx, *args):
    pos, val = args
    if mtrx[pos[0]][pos[1]] != EMPTY_CELL:
        mtrx[pos[0]][pos[1]] = val[0]


def delete(mtrx, *args):
    pos, val = args
    if mtrx[pos[0]][pos[1]] != EMPTY_CELL:
        mtrx[pos[0]][pos[1]] = EMPTY_CELL


def read(mtrx, *args):
    pos, val = args
    if mtrx[pos[0]][pos[1]] != EMPTY_CELL:
        return mtrx[pos[0]][pos[1]]


actions = {
    "Create": create,
    "Update": update,
    "Delete": delete,
    "Read": read,
}

matrix = [input().split() for _ in range(SIZE)]

position = [int(x) for x in input() if x.isnumeric()]

while True:
    command = input()
    if command == "Stop":
        break

    action, direction, *value = command.split(", ")

    position[0] += directions[direction][0]
    position[1] += directions[direction][1]

    result = actions[action](matrix, position, value)

    print(result) if result else None

[print(*matrix[row], sep=" ") for row in range(SIZE)]
