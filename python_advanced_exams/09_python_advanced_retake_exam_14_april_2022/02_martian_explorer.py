from collections import deque

SIZE = 6
ROVER, ROCK, EMPTY = "E", "R", "-"
DEPOSITS = {
    "W": "Water", "M": "Metal", "C": "Concrete",
}
DIRECTIONS = {
    "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)
}

field = []
rover_row, rover_col = None, None  # rover position
for r in range(SIZE):
    line = input().split()
    if ROVER in line:
        rover_row, rover_col = r, line.index(ROVER)
    field.append(line)
commands = deque(input().split(", "))

deposits_collected = set()
while commands:
    command = commands.popleft()
    row = (rover_row + DIRECTIONS[command][0]) % SIZE
    col = (rover_col + DIRECTIONS[command][1]) % SIZE

    if field[row][col] == ROCK:
        print(f"Rover got broken at ({row}, {col})")
        break
    elif field[row][col] in DEPOSITS:
        deposit = DEPOSITS[field[row][col]]
        deposits_collected.add(deposit)
        print(f"{deposit} deposit found at ({row}, {col})")

    rover_row, rover_col = row, col

if len(deposits_collected) == len(DEPOSITS):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
