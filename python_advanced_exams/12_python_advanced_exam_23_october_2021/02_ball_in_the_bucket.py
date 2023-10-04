SIZE = 6

matrix = [[x for x in input().split()] for _ in range(SIZE)]

score = 0
for _ in range(3):
    line = input()
    row, col = [int(x) for x in line[1:-1].split(", ")]
    if row < 0 or col < 0 or row >= SIZE or col >= SIZE:
        continue
    if matrix[row][col] != "B":
        continue

    matrix[row][col] = "0"
    for r in range(0, SIZE):
        score += int(matrix[r][col]) if matrix[r][col].isnumeric() else None

if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
elif score < 200:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif score < 300:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
