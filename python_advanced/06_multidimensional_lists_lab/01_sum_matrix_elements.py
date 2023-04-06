# https://judge.softuni.org/Contests/Practice/Index/1834#0

rows, cols = [int(x) for x in input().split(", ")]

total = 0
matrix = []
for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    total += sum(row)

print(total)
print(matrix)
