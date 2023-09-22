rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
areas_number = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        if all(x == matrix[r][c] for x in [matrix[r + 1][c], matrix[r][c + 1], matrix[r + 1][c + 1]]):
            areas_number += 1
print(areas_number)
