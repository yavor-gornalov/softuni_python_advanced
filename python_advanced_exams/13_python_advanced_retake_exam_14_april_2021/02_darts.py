size = 7
initial_points = 501


def sum_corresponding_numbers(r, c):
    return sum([matrix[0][c], matrix[size - 1][c],
                matrix[r][0], matrix[r][size - 1]])


first_player = {"name": "", "throws": 0, "score": 501}
second_player = {"name": "", "throws": 0, "score": 501}

first_player["name"], second_player["name"] = input().split(", ")

matrix = [[None] * size for _ in range(size)]
for r in range(size):
    line = input().split()
    for c in range(size):
        if line[c].isalpha():
            matrix[r][c] = line[c]
        else:
            matrix[r][c] = int(line[c])

current_player, next_player = first_player, second_player
while True:
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    current_score = 0
    if row < 0 or col < 0 or row >= size or col >= size:
        pass
    elif matrix[row][col] == "B":
        current_score = 501
    elif matrix[row][col] == "T":
        current_score = sum_corresponding_numbers(row, col) * 3
    elif matrix[row][col] == "D":
        current_score = sum_corresponding_numbers(row, col) * 2
    else:
        current_score = matrix[row][col]

    current_player["throws"] += 1
    current_player["score"] -= current_score
    if current_player["score"] <= 0:
        break
    current_player, next_player = next_player, current_player

print(f'{current_player["name"]} won the game with {current_player["throws"]} throws!')
