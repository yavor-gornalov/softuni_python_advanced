from collections import deque

EMPTY, END, COAL, MINER = "*", "e", "c", "s"
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())
commands = deque(x for x in input().split())

coal_left = 0
field = []
row, col = None, None
for r in range(size):
    line = input().split()
    if MINER in line:
        row, col = r, line.index(MINER)
    if COAL in line:
        coal_left += line.count(COAL)
    field.append(line)

end_reached = False
while commands and coal_left and not end_reached:
    command = commands.popleft()
    if command not in DIRECTIONS:
        continue
    r, c = DIRECTIONS[command]
    next_r = row + r
    next_c = col + c
    if next_r < 0 or next_r >= size or next_c < 0 or next_c >= size:
        continue
    if field[next_r][next_c] == COAL:
        coal_left -= 1
    elif field[next_r][next_c] == END:
        end_reached = True
    field[row][col] = EMPTY
    field[next_r][next_c] = MINER
    row, col = next_r, next_c

if end_reached:
    print(f"Game over! {row, col}")
elif coal_left:
    print(f"{coal_left} pieces of coal left. {row, col}")
elif not coal_left:
    print(f"You collected all coal! {row, col}")
