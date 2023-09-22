from collections import deque

commands = {
    "+": lambda x, y: abs(x + y),
    "-": lambda x, y: abs(x - y),
    "*": lambda x, y: abs(x * y),
    "/": lambda x, y: abs(x / y) if y != 0 else 0,
}

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
honey_making = deque(input().split())

honey_produced = 0
while working_bees and nectar:
    matched_bee = working_bees.popleft()
    matched_nectar = nectar.pop()
    while nectar and matched_nectar < matched_bee:
        matched_nectar = nectar.pop()
    if matched_bee > matched_nectar:
        working_bees.appendleft(matched_bee)
        break
    operator = honey_making.popleft()
    honey_produced += commands[operator](matched_bee, matched_nectar)

print(f"Total honey made: {honey_produced}")
print(f"Bees left: {', '.join([str(b) for b in working_bees])}") if working_bees else None
print(f"Nectar left: {', '.join([str(n) for n in nectar])}") if nectar else None
