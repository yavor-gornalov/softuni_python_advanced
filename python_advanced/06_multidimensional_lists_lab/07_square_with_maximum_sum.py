# https://judge.softuni.org/Contests/Practice/Index/1834#6

from sys import maxsize

rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

max_sum = -maxsize
max_matrix = []
for i in range(rows - 1):
    for j in range(cols - 1):
        sub_matrix = [
            [matrix[i][j], matrix[i][j + 1]],
            [matrix[i + 1][j], matrix[i + 1][j + 1]]
        ]
        current_sum = 0
        for row in sub_matrix:
            current_sum += sum(row)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = sub_matrix

for r in max_matrix:
    print(*r, sep=" ")
print(max_sum)
