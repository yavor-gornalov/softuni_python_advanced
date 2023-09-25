KNIGHT, EMPTY = "K", "0"
POSSIBLE_MOVES = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def knight_attacks_counter(matrix, knight):
    counter = 0
    for move in POSSIBLE_MOVES:
        row = knight[0] + move[0]
        col = knight[1] + move[1]
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue
        if matrix[row][col] == KNIGHT:
            counter += 1
    return counter


def get_max_attacker():
    max_attacks_count = 0
    max_attacker = None
    for knight in knights:
        current_attacks_count = knight_attacks_counter(board, knight)
        if current_attacks_count > max_attacks_count:
            max_attacks_count = current_attacks_count
            max_attacker = knight
    return max_attacker


board_size = int(input())
board = []
knights = []

for r in range(board_size):
    line = list(input())
    for c in range(board_size):
        if line[c] == KNIGHT:
            knights.append((r, c))
    board.append(line)

knight_to_remove = get_max_attacker()
removed_knights_counter = 0
while True:
    knight_to_remove = get_max_attacker()
    if not knight_to_remove:
        break
    row, col = knight_to_remove
    board[row][col] = EMPTY
    removed_knights_counter += 1
    knights.remove((row, col))

print(removed_knights_counter)
