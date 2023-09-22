from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque([x for x in input()])

matrix = []
for i in range(rows):
    row = deque()
    for j in range(cols):
        row.append(text[0]) if i % 2 == 0 else row.appendleft(text[0])
        text.rotate(-1)
    matrix.append(row)

[print(''.join(row)) for row in matrix]
