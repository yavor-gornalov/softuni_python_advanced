n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

ACTIONS = {
    "Add": lambda x: x,
    "Subtract": lambda x: - x
}

command = input()
while command != "END":
    action, *data = command.split()
    row, col, value = [int(x) for x in data]
    if row < 0 or col < 0 or row >= n or col >= n:
        print("Invalid coordinates")
    else:
        matrix[row][col] += ACTIONS[action](value)
    command = input()

[print(*row) for row in matrix]
