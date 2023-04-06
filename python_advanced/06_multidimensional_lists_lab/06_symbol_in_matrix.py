# https://judge.softuni.org/Contests/Practice/Index/1834#5

n = int(input())

matrix = []
for i in range(n):
    row = list(input())
    matrix.append(row)

symbol = input()

for i in range(n):
    symbol_exists = False
    for j in range(n):
        if matrix[i][j] == symbol:
            print((i, j))
            symbol_exists = True
            break
    if symbol_exists:
        break
else:
    print(f"{symbol} does not occur in the matrix")
