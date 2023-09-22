rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]


def all_coordinates_valid(*args):
    is_even = True
    for coordinate in args:
        limit = rows if is_even else cols
        if coordinate < 0 or coordinate >= limit:
            return False
        is_even = not is_even
    return True


while True:
    line = input()
    if line.startswith("END"):
        break
    elif not line.startswith("swap"):
        print("Invalid input!")
        continue
    coordinates = [int(x) for x in line.split()[1:] if x.isnumeric()]
    if len(coordinates) != 4 or not all_coordinates_valid(*coordinates):
        print("Invalid input!")
        continue
    matrix[coordinates[0]][coordinates[1]], matrix[coordinates[2]][coordinates[3]] = (
        matrix[coordinates[2]][coordinates[3]], matrix[coordinates[0]][coordinates[1]])
    [print(*row) for row in matrix]
