# https://judge.softuni.org/Contests/Practice/Index/3596#1

CAR, TUNNEL, EMPTY, FINISH = "C", "T", ".", "F"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

race_size = int(input())
car_number = input()

race_field = []
tunnel_coordinates = []
for r in range(race_size):
    line = input().split()
    if TUNNEL in line:
        tunnel_coordinates.append([r, line.index(TUNNEL)])
    race_field.append(line)

finished = False
distance = 0
current_position = [0, 0]
while not finished:
    direction = input()
    r0, c0 = current_position

    if direction == "End":
        race_field[r0][c0] = CAR
        break
    row = r0 + directions[direction][0]
    col = c0 + directions[direction][1]

    race_field[r0][c0] = EMPTY

    if race_field[row][col] == TUNNEL:
        tunnel_coordinates.pop(tunnel_coordinates.index([row, col]))
        race_field[row][col] = EMPTY
        row, col = tunnel_coordinates.pop()
        distance += 30

    elif race_field[row][col] == EMPTY:
        distance += 10

    elif race_field[row][col] == FINISH:
        distance += 10
        finished = True

    race_field[row][col] = CAR
    current_position = [row, col]

if finished:
    print(f"Racing car {car_number} finished the stage!")
else:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance} km.")

[print(*race_field[row], sep="") for row in range(race_size)]
