# https://judge.softuni.org/Contests/Practice/Index/1834#1

n = int(input())

matrix = []
for i in range(n):
    row = [int(x) for x in input().split(", ") if not int(x) % 2]
    matrix.append(row)

print(matrix)
