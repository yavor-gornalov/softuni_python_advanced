# https://judge.softuni.org/Contests/Practice/Index/3194#1

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break
    command_args = command.split()
    action = command_args[0]
    row, col, value = [int(x) for x in command_args[1:4]]
    if 0 <= row <= n and 0 <= col < n:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*matrix[i], sep=" ") for i in range(n)]
