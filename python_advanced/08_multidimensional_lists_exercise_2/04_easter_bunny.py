# https://judge.softuni.org/Contests/Practice/Index/3194#3

def bunny_move(mtrx, pos, direct, pth):
    r = pos[0] + direct[0]
    c = pos[1] + direct[1]
    if r < 0 or c < 0 or r >= len(mtrx) or c >= len(mtrx[0]) or mtrx[r][c] == TRAP:
        return 0

    res = int(mtrx[r][c])
    pth.append([r, c])

    res += bunny_move(mtrx, (r, c), direct, pth)
    return res


BUNNY, TRAP = "B", "X"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

n = int(input())

field, bunny_position = [], ()
for i in range(n):
    line = input().split()
    field.append([])
    for j, ele in enumerate(line):
        if ele == BUNNY:
            bunny_position = (i, j)
        field[i].append(ele)

best_result = 0
best_path = []
best_direction = ""
for direction, coordinates in directions.items():
    path = []
    result = bunny_move(field, bunny_position, coordinates, path)
    if result >= best_result:
        best_result = result
        best_path = path
        best_direction = direction

print(best_direction), print(*best_path, sep="\n"), print(best_result)
