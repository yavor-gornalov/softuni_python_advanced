# https://judge.softuni.org/Contests/Practice/Index/3159#3

from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

functions = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: abs(x - y),
    "*": lambda x, y: x * y,
    "/": lambda x, y: abs(x / y) if y != 0 else 0
}

total_honey = 0
while working_bees and nectar:
    bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= bee:
        symbol = symbols.popleft()
        total_honey += functions[symbol](bee, last_nectar)
    else:
        working_bees.appendleft(bee)

print(f"Total honey made: {total_honey}")
print(f"Bees left: {', '.join([str(b) for b in working_bees])}") if working_bees else None
print(f"Nectar left: {', '.join([str(n) for n in nectar])}") if nectar else None
