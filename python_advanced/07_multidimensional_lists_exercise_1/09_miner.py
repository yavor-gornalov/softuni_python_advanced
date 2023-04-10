# https://judge.softuni.org/Contests/Practice/Index/1835#8
from collections import deque


def print_matrix(mtrx, sep=" "):
    for r in range(len(mtrx)):
        print(*mtrx[r], sep=sep)


def miner_move(mtrx, pos, cmd):
    r, c = pos
    if cmd == LEFT:
        c = max(c - 1, 0)
    elif cmd == RIGHT:
        c = min(c + 1, len(mtrx[0]) - 1)
    elif cmd == UP:
        r = max(r - 1, 0)
    elif cmd == DOWN:
        r = min(r + 1, len(mtrx) - 1)
    return r, c


def mining_game(mtrx, mnr_pos, coal_to_collect, cmds):
    while cmds:
        cmd = cmds.popleft()
        r0, c0 = mnr_pos
        new_pos = miner_move(mtrx, mnr_pos, cmd)
        r1, c1 = new_pos
        if mtrx[r1][c1] == FREE:
            mtrx[r1][c1], mtrx[r0][c0] = mtrx[r0][c0], mtrx[r1][c1]
        elif mtrx[r1][c1] == COAL:
            coal_to_collect -= 1
            mtrx[r0][c0] = FREE
            mtrx[r1][c1] = FREE
        elif mtrx[r1][c1] == EXIT:
            print(f"Game over! {new_pos}")
            return
        mnr_pos = new_pos

        if coal_to_collect == 0:
            print(f"You collected all coal! {mnr_pos}")
            return
    else:
        print(f"{coal_to_collect} pieces of coal left. {mnr_pos}")


FREE, EXIT, COAL, MINER = list("*ecs")
LEFT, RIGHT, UP, DOWN = ["left", "right", "up", "down"]

n = int(input())
commands = deque(input().split())

field = []
miner_position = None
coal_count = 0
for i in range(n):
    row = []
    for j, ele in enumerate(input().split()):
        if ele == MINER:
            miner_position = (i, j)
        elif ele == COAL:
            coal_count += 1
        row.append(ele)
    field.append(row)

mining_game(field, miner_position, coal_count, commands)
