# https://judge.softuni.org/Contests/Practice/Index/1831#3

from collections import deque

cloths = deque([int(x) for x in input().split()])
rack_capacity = int(input())
rack = deque()

racks_count = 1
while cloths:
    clothing = cloths.pop()
    rack.append(clothing)
    if sum(rack) > rack_capacity:
        racks_count += 1
        rack.clear()
        rack.append(clothing)

print(racks_count)