size_matrix = int(input())
car_number = input()
matrix = []
total_km_passed = 0
car_coordinates = [0, 0]

for _ in range(size_matrix):
    matrix.append(input().split())


def find_end_of_dune(mx):
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            if mx[row][col] == "T":
                return row, col


while True:
    command = input()
    if command == 'End':
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        break
    elif command == "left":
        car_coordinates[1] -= 1
    elif command == "right":
        car_coordinates[1] += 1
    elif command == "up":
        car_coordinates[0] -= 1
    elif command == "down":
        car_coordinates[0] += 1
    if matrix[car_coordinates[0]][car_coordinates[1]] == "F":
        total_km_passed += 10
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} finished the stage!")
        break
    elif matrix[car_coordinates[0]][car_coordinates[1]] == "T":
        total_km_passed += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        car_coordinates[0], car_coordinates[1] = find_end_of_dune(matrix)
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
    else:
        total_km_passed += 10

print(f"Distance covered {total_km_passed} km.")
for row in range(len(matrix)):
    print("".join(matrix[row]))