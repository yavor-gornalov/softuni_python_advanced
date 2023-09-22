rows, cols = [int(x) for x in input().split()]

for r in range(rows):
    row = []
    for c in range(cols):
        row.append("".join([chr(ord("a") + r), chr(ord("a") + r + c), chr(ord("a") + r)]))
    print(*row)
