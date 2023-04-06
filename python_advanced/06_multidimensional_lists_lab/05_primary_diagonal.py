# https://judge.softuni.org/Contests/Practice/Index/1834#4

n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_sum = 0
for i in range(n):
    primary_sum += matrix[i][i]

print(primary_sum)
