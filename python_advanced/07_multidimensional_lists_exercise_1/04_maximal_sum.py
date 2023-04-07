# https://judge.softuni.org/Contests/Practice/Index/1835#3
import sys

rows, cols = [int(x) for x in input().split()]

matrix = []
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

max_sum = -sys.maxsize
max_matrix = []
for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = 0
        sub_matrix = []
        for r in range(i, i + 3):
            sub_row = matrix[r][j:j + 3]
            sub_matrix.append(sub_row)
            current_sum += sum(sub_row)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = sub_matrix

print(f"Sum = {max_sum}")
[print(*max_matrix[i], sep=" ") for i in range(len(max_matrix))]
