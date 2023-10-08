SNAKE, FOOD, BURROW, EMPTY, VISITED = "S", "*", "B", "-", "."
DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

size = int(input())
matrix = []
burrows = []
snake_position = None, None
for r in range(size):
    line = list(input())
    if SNAKE in line:
        snake_position = r, line.index(SNAKE)
    if BURROW in line:
        burrows.append([r, line.index(BURROW)])
    matrix.append(line)

food_collected = 0
snake_lost = False
row, col = snake_position
while food_collected < 10 and not snake_lost:
    command = input()
    if command not in DIRECTIONS:
        continue
    r, c = DIRECTIONS[command]
    matrix[row][col] = VISITED
    next_r, next_c = row + r, col + c
    if next_r < 0 or next_c < 0 or next_r >= size or next_c >= size:
        snake_lost = True
        break
    if matrix[next_r][next_c] == FOOD:
        food_collected += 1
        matrix[next_r][next_c] = SNAKE
    if [next_r, next_c] in burrows:
        for burrow in burrows:
            row_b, col_b = burrow
            if [next_r, next_c] == [row_b, col_b]:
                matrix[row_b][col_b] = VISITED
                continue
            next_r, next_c = burrow
            matrix[next_r][next_c] = SNAKE
    row, col = next_r, next_c

print("Game over!") if snake_lost else print("You won! You fed the snake.")
print(f"Food eaten: {food_collected}")
[print(*row, sep='') for row in matrix]
