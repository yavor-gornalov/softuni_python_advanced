# https://judge.softuni.org/Contests/Practice/Index/3194#2

def knights_attacked(mtrx, pos):
    row, col = pos
    count = 0
    for direction in directions:
        x, y = direction
        r, c = row + x, col + y
        if 0 <= r <= len(mtrx) - 1 and 0 <= c <= len(mtrx[0]) - 1:
            if mtrx[r][c] == KNIGHT:
                count += 1
    return count


KNIGHT, EMPTY = "K", "0"

n = int(input())
board = []
knights = []
for i in range(n):
    row, text = [], input()
    for j, ele in enumerate(text):
        if ele == KNIGHT:
            knights.append([(i, j), -1])
        row.append(ele)
    board.append(row)

directions = {
    (-2, -1),
    (-1, -2),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
}

count_removed = 0
while True:
    if all(ele[1] == 0 for ele in knights):
        break
    max_attacker_idx = None
    max_attacker_pos = ()
    max_attacked_count = -1
    for idx, knight in enumerate(knights):
        knight[1] = knights_attacked(board, knight[0])
        if knight[1] > max_attacked_count:
            max_attacker_idx = idx
            max_attacker_pos = knight[0]
            max_attacked_count = knight[1]

    if max_attacked_count > 0:
        knights.pop(max_attacker_idx)
        row, col = max_attacker_pos
        board[row][col] = EMPTY
        count_removed += 1

print(count_removed)
