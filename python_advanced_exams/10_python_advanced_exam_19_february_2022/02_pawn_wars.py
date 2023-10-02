WHITE_PAWN, BLACK_PAWN = "w", "b"


def square_by_index(row, col):
    return f"{chr(col + ord('a'))}{8 - row}"


board = []
white_pos = (-1, -1)
black_pos = (-1, -1)
for r in range(8):
    line = input().split()
    if WHITE_PAWN in line:
        white_pos = r, line.index(WHITE_PAWN)
    if BLACK_PAWN in line:
        black_pos = r, line.index(BLACK_PAWN)

if abs(white_pos[1] - black_pos[1]) > 1:
    if white_pos[0] < (8 - black_pos[0]):
        print(f"Game over! White pawn is promoted to a queen at {square_by_index(0, white_pos[1])}.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {square_by_index(7, black_pos[1])}.")
else:
    if (white_pos[0] - black_pos[0]) % 2 != 0:
        print(
            f"Game over! White win, capture on {square_by_index((white_pos[0] + black_pos[0]) // 2, black_pos[1])}.")
    else:
        print(
            f"Game over! Black win, capture on {square_by_index((black_pos[0] + white_pos[0]) // 2, white_pos[1])}.")
