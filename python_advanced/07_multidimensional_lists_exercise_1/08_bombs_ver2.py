from collections import deque

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = deque(tuple(int(y) for y in x.split(",")) for x in input().split())

directions = [
    (1, -1),  # uo-left
    (1, 0),  # up
    (1, 1),  # up-right
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # down-left
    (-1, 0),  # down
    (-1, 1),  # down-right
    (0, 0),  # current
]

while bombs:
    bomb_r, bomb_c = bombs.popleft()
    """
    Constraints:
    The bomb's values will always be greater than 0.
    But test 5, could not be passed.
    """
    if matrix[bomb_r][bomb_c] <= 0:
        continue
    for direction in directions:
        r, c = direction
        row = bomb_r + r
        col = bomb_c + c
        if row < 0 or row >= n or col < 0 or col >= n:
            continue
        if matrix[row][col] <= 0:
            continue
        matrix[row][col] -= matrix[bomb_r][bomb_c]

alive_cells_count = 0
alive_cells_sum = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells_count += 1
            alive_cells_sum += matrix[row][col]

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
[print(*row) for row in matrix]
