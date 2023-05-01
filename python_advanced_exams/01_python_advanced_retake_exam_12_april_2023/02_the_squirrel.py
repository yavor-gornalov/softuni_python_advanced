# https://judge.softuni.org/Contests/Practice/Index/3893#1

SQUIRREL, HAZELNUT, EMPTY, TRAP = "s", "h", "*", "t"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

field_size = int(input())
commands = input().split(", ")

squirrel_position = None
field = []
for r in range(field_size):
    row = input()
    if SQUIRREL in row:
        squirrel_position = [r, row.index(SQUIRREL)]
    field.append(list(row))

hazelnuts_collected = 0
message = ""
for command in commands:
    r0, c0 = squirrel_position
    row = r0 + directions[command][0]
    col = c0 + directions[command][1]
    if not (0 <= row < field_size and 0 <= col < field_size):
        print("The squirrel is out of the field.")
        break
    if field[row][col] == TRAP:
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if field[row][col] == HAZELNUT:
        hazelnuts_collected += 1
        if hazelnuts_collected == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    field[r0][c0] = EMPTY
    field[row][col] = SQUIRREL
    squirrel_position = [row, col]
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")
