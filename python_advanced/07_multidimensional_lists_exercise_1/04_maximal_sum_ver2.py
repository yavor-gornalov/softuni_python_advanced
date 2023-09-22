rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float("-inf")
max_matrix_start_point = None
for r in range(rows - 2):
    for c in range(cols - 2):
        current_sum = 0
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                current_sum += matrix[i][j]
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix_start_point = (r, c)
print(f"Sum = {max_sum}")
row, col = max_matrix_start_point
for i in range(row, row + 3):
    print(*matrix[i][col:col + 3])
