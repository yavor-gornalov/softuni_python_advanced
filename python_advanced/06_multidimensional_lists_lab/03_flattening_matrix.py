# https://judge.softuni.org/Contests/Practice/Index/1834#2

n = int(input())

matrix = []
for i in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.extend(row)

print(matrix)
