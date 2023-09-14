# https://judge.softuni.org/Contests/Practice/Index/3744#1

SUBMARINE, CRUISER, MINE, EMPTY = "S", "C", "*", "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size_of_battlefield = int(input())

battlefield = []
submarine_position = None
for r in range(size_of_battlefield):
    line = [x for x in input()]
    if SUBMARINE in line:
        submarine_position = [r, line.index(SUBMARINE)]
    battlefield.append(line)

mines_hits = 0
cruiser_hits = 0
while True:
    direction = input()
    r0, c0 = submarine_position
    row = r0 + directions[direction][0]
    col = c0 + directions[direction][1]

    if battlefield[row][col] == MINE:
        mines_hits += 1
    elif battlefield[row][col] == CRUISER:
        cruiser_hits += 1

    battlefield[r0][c0] = EMPTY
    battlefield[row][col] = SUBMARINE
    submarine_position = [row, col]

    if mines_hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break
    elif cruiser_hits == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

[print("".join(battlefield[r])) for r in range(size_of_battlefield)]
