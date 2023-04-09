# https://judge.softuni.org/Contests/Practice/Index/1835#6
from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())

matrix = []
for i in range(rows):
    row = deque()
    for j in range(cols):
        if not i % 2:
            row.append(text[0])
        else:
            row.appendleft(text[0])
        text.rotate(-1)
    print(*row, sep="")
