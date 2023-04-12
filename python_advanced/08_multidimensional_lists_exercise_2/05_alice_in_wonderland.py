# https://judge.softuni.org/Contests/Practice/Index/3194#4

ALICE, RABBIT_HOLE, EMPTY, VISITED = "A", "R", ".", "*"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def alice_move(mtrx, direct, pos):
    r, c = pos[0], pos[1]
    mtrx[r][c] = VISITED

    r += directions[direct][0]
    c += directions[direct][1]
    tea = 0

    if 0 <= r < len(mtrx) and 0 <= c < len(mtrx[0]):
        if mtrx[r][c].isnumeric():
            tea = int(mtrx[r][c])
        elif mtrx[r][c] == RABBIT_HOLE:
            mtrx[r][c] = VISITED
            return pos, tea

        mtrx[r][c] = VISITED
        return (r, c), tea

    return pos, tea


size = int(input())
territory = []
alice_position = None
for i in range(size):
    line = input().split()
    if ALICE in line:
        alice_position = (i, line.index(ALICE))
    territory.append(line)

collected_tea = 0
while collected_tea < 10:
    direction = input()
    new_position, current_tea = alice_move(territory, direction, alice_position)
    if new_position == alice_position:
        break
    alice_position = new_position
    collected_tea += current_tea

if collected_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*territory[row], sep=" ") for row in range(size)]
