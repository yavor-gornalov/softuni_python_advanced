# https://judge.softuni.org/Contests/Practice/Index/1835#1

n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    primary_diagonal.append(row[i])
    secondary_diagonal.append(row[n - i - 1])

diagonal_abs_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diagonal_abs_difference)
