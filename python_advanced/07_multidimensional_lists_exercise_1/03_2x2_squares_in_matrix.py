# https://judge.softuni.org/Contests/Practice/Index/1835#2

rows, cols = [int(x) for x in input().split()]

matrix = []
for i in range(rows):
    row = list(input().split())
    matrix.append(row)

counter = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        sub_matrix = [matrix[r][c] for r in range(i, i + 2) for c in range(j, j + 2)]
        if all(x == sub_matrix[0] for x in sub_matrix):
            counter += 1

print(counter)
