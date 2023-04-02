# https://judge.softuni.org/Contests/Practice/Index/1831#9

from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_water = 0
while cups and bottles:
    cup = cups.popleft()

    while bottles and cup > 0:
        bottle = bottles.pop()
        if bottle > cup:
            wasted_water += bottle - cup
        cup -= bottle

if not cups and bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
if not bottles and cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")
