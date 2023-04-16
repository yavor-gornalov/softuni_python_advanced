# https://judge.softuni.org/Contests/Practice/Index/3194#6

SANTA, NICE, NAUGHTY, COOKIE, EMPTY = "S", "V", "X", "C", "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "initial": (0, 0)
}


def neighbours(mtrx, pos):
    global nice_kids, presents
    for d, coordinates in directions.items():
        r, c = pos
        r += coordinates[0]
        c += coordinates[1]
        if 0 <= r < len(mtrx) and 0 <= c < len(mtrx[0]):
            if presents > 0:
                if mtrx[r][c] == NICE:
                    presents -= 1
                    nice_kids -= 1
                elif mtrx[r][c] == NAUGHTY:
                    presents -= 1
                mtrx[r][c] = EMPTY


def santa_movement(mtrx, pos, dr):
    global nice_kids, presents
    r0, c0 = pos
    r = r0 + directions[dr][0]
    c = c0 + directions[dr][1]
    if 0 <= r < len(mtrx) and 0 <= c < len(mtrx[0]):
        if mtrx[r][c] == NICE:
            presents -= 1
            nice_kids -= 1
        elif mtrx[r][c] == COOKIE:
            neighbours(mtrx, (r, c))
        mtrx[r0][c0] = EMPTY
        mtrx[r][c] = SANTA
        return r, c
    return r0, c0


presents, size = int(input()), int(input())

matrix, santa_position, total_nice_kids = [], (), 0
for i in range(size):
    line = input().split()
    if SANTA in line:
        santa_position = (i, line.index(SANTA))
    if NICE in line:
        total_nice_kids += line.count(NICE)
    matrix.append(line)

nice_kids = total_nice_kids
command = input()
while command != "Christmas morning":
    santa_position = santa_movement(matrix, santa_position, command)
    if not presents:
        break
    command = input()

if not presents and nice_kids:
    print("Santa ran out of presents!")
[print(*matrix[i], sep=" ") for i in range(size)]
if nice_kids:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
