# https://judge.softuni.org/Contests/Practice/Index/1835#0

n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    primary_diagonal.append(row[i])
    secondary_diagonal.append(row[n - i - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}\n"
      f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
