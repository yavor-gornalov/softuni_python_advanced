# https://judge.softuni.org/Contests/Practice/Index/1831#3

from collections import deque

cloths = deque([int(x) for x in input().split()])
rack_capacity = int(input())

free_capacity = rack_capacity
racks_count = 1
while cloths:
    clothing = cloths.pop()
    if clothing <= free_capacity:
        free_capacity -= clothing
    else:
        free_capacity = rack_capacity - clothing
        racks_count += 1

print(racks_count)
