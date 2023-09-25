line = input().split("|")
result = []
[result.extend([y for y in x.split()])for x in line[::-1]]
print(*result)
