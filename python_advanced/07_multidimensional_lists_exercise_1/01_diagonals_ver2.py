n = int(input())
primary_diagonal, secondary_diagonal = [], []
primary_sum, secondary_sum = 0, 0
for i in range(n):
    line = [int(x) for x in input().split(", ")]
    primary_diagonal.append(line[i])
    primary_sum += line[i]
    secondary_diagonal.append(line[n - i - 1])
    secondary_sum += line[n - i - 1]
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {primary_sum}\n"
      f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {secondary_sum}")
