# https://judge.softuni.org/Contests/Practice/Index/1834#3

rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for j in range(cols):
    sum_col = 0
    for i in range(rows):
        sum_col += matrix[i][j]
    print(sum_col)
