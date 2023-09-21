from collections import deque
from functools import reduce

commands = {
    "*": lambda nums: reduce(lambda x, y: x * y, nums),
    "+": lambda nums: reduce(lambda x, y: x + y, nums),
    "-": lambda nums: reduce(lambda x, y: x - y, nums),
    "/": lambda nums: reduce(lambda x, y: x // y, nums)
}

expression = deque(x for x in input().split())

numbers = []
while expression:
    el = expression.popleft()
    if el not in ["*", "+", "-", "/"]:
        numbers.append(int(el))
        continue
    numbers = [commands[el](numbers)]

print(*numbers)
