# https://judge.softuni.org/Contests/Practice/Index/3194#5

SIZE = 5
AIM, TARGET, EMPTY = "A", "x", "."
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def aim_move(mtrx, pos, stp, direct):
    r0, c0 = pos
    r = r0 + directions[direct][0] * stp
    c = c0 + directions[direct][1] * stp
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if mtrx[r][c] == TARGET:
            return r0, c0
        mtrx[r0][c0] = EMPTY
        mtrx[r][c] = AIM
        return r, c
    return r0, c0


def shoot(mtrx, pos, direct):
    r0, c0 = pos
    while True:
        r = r0 + directions[direct][0]
        c = c0 + directions[direct][1]
        if r < 0 or c < 0 or r >= SIZE or c >= SIZE:
            break
        if mtrx[r][c] == TARGET:
            mtrx[r][c] = EMPTY
            return [r, c]
        r0, c0 = r, c


matrix, player_position = [], []
target_count = 0
for i in range(SIZE):
    line = input().split()
    if AIM in line:
        player_position = [i, line.index(AIM)]
    target_count += line.count(TARGET)
    matrix.append(line)

targets_left = target_count
targets_hit = []
for _ in range(int(input())):
    if targets_left == 0:
        break
    command = input()
    command_args = command.split()
    action, direction = command_args[0], command_args[1]

    if action == "move":
        steps = int(command_args[2])
        player_position = aim_move(matrix, player_position, steps, direction)
    elif action == "shoot":
        target = shoot(matrix, player_position, direction)
        if target:
            targets_hit.append(target)
            targets_left -= 1

if targets_left:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {target_count} targets hit.")
print(*targets_hit, sep="\n")
