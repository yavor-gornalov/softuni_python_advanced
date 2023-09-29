SANTA, NAUGHTY_KID, NICE_KID, COOKIE, EMPTY = "S", "X", "V", "C", "-"
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

presents_count = int(input())
size = int(input())
row, col = None, None  # Santa initial position
nice_kids_count = 0
matrix = []
for cookie_r in range(size):
    line = [x for x in input().split()]
    if SANTA in line:
        row, col = cookie_r, line.index(SANTA)
    if NICE_KID in line:
        nice_kids_count += line.count(NICE_KID)
    matrix.append(line)

nice_kids_left = nice_kids_count
while presents_count:
    command = input()
    if command == "Christmas morning":
        break
    next_row = row + DIRECTIONS[command][0]
    next_col = col + DIRECTIONS[command][1]

    if matrix[next_row][next_col] == NICE_KID:
        nice_kids_left -= 1
        presents_count -= 1
    elif matrix[next_row][next_col] == NAUGHTY_KID:
        pass
    elif matrix[next_row][next_col] == COOKIE:
        for r0, c0 in DIRECTIONS.values():
            if not presents_count:
                break
            cookie_r = next_row + r0
            cookie_c = next_col + c0
            if matrix[cookie_r][cookie_c] in [NAUGHTY_KID, NICE_KID]:
                if matrix[cookie_r][cookie_c] == NICE_KID:
                    nice_kids_left -= 1
                matrix[cookie_r][cookie_c] = EMPTY
                presents_count -= 1

    matrix[row][col] = EMPTY
    matrix[next_row][next_col] = SANTA
    row, col = next_row, next_col

if presents_count == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
