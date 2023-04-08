# https://judge.softuni.org/Contests/Practice/Index/1835#5

def print_matrix(mtrx, sep=" "):
    for r in range(len(matrix)):
        print(*mtrx[r], sep=sep)


def swap_matrix(mtrx, coord1, coord2):
    row1, col1 = coord1
    row2, col2 = coord2

    if 0 <= row1 < len(mtrx) or 0 <= row2 < len(mtrx) or \
            0 <= col1 < len(mtrx[0] or 0 <= col2 < len(mtrx[0])):
        # temp = mtrx[row1][col1]
        # mtrx[row2][col2] = mtrx[row1][col1]
        # mtrx[row2][col2] = temp
        mtrx[row1][col1], mtrx[row2][col2] = mtrx[row2][col2], mtrx[row1][col1]
        return True
    return False


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command.startswith("END"):
        break
    elif command.startswith("swap"):
        command, *args = command.split()
        if len(args) == 4:
            r1, c1, r2, c2 = [int(x) for x in args]
            if swap_matrix(matrix, (r1, c1), (r2, c2)):
                print_matrix(matrix)
                continue
    print("Invalid input!")
