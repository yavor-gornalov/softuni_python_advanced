# https://judge.softuni.org/Contests/Practice/Index/1835#7


def explode(mtrx, bmb):
    r, c = bmb
    value = mtrx[r][c]
    if value > 0:
        mtrx[r][c] = 0
        if r - 1 >= 0 and c - 1 >= 0 and mtrx[r - 1][c - 1] > 0:
            mtrx[r - 1][c - 1] -= value
        if r - 1 >= 0 and mtrx[r - 1][c] > 0:
            mtrx[r - 1][c] -= value
        if r - 1 >= 0 and c + 1 <= len(mtrx[0]) - 1 and mtrx[r - 1][c + 1] > 0:
            mtrx[r - 1][c + 1] -= value
        if c - 1 >= 0 and mtrx[r][c - 1] > 0:
            mtrx[r][c - 1] -= value
        if c + 1 <= len(matrix[0]) - 1 and mtrx[r][c + 1] > 0:
            mtrx[r][c + 1] -= value
        if r + 1 <= len(mtrx) - 1 and c - 1 >= 0 and mtrx[r + 1][c - 1] > 0:
            mtrx[r + 1][c - 1] -= value
        if r + 1 <= len(mtrx) - 1 and mtrx[r + 1][c] > 0:
            mtrx[r + 1][c] -= value
        if r + 1 <= len(mtrx) - 1 and c + 1 <= len(matrix[0]) - 1 and mtrx[r + 1][c + 1] > 0:
            mtrx[r + 1][c + 1] -= value


def print_matrix(mtrx, sep=" "):
    for r in range(len(matrix)):
        print(*mtrx[r], sep=sep)


def alive_cells(mtrx):
    positive_cells = []
    for i in range(len(mtrx)):
        for ele in mtrx[i]:
            positive_cells.append(ele) if ele > 0 else None
    positive_cells_count = len(positive_cells) if positive_cells else 0
    positive_cells_sum = sum(positive_cells) if positive_cells else 0
    return positive_cells_count, positive_cells_sum


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = [[int(x) for x in bomb.split(",")] for bomb in input().split()]

for bomb in bombs:
    explode(matrix, bomb)

cells_cnt, cells_sum = alive_cells(matrix)
print(f"Alive cells: {cells_cnt}\nSum: {cells_sum}")
print_matrix(matrix, sep=" ")
