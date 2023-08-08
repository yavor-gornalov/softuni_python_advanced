# https://judge.softuni.org/Contests/Practice/Index/1831#3

from collections import deque

cloths = deque([int(x) for x in input().split()])
rack_capacity = int(input())

counter = 1
current_capacity = rack_capacity
while cloths:
    current_cloth = cloths.pop()
    if current_cloth <= current_capacity:
        current_capacity -= current_cloth
    else:
        current_capacity = rack_capacity - current_cloth
        counter += 1

print(counter)
