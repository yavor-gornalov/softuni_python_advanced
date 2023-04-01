# https://judge.softuni.org/Contests/Practice/Index/1831#4

from collections import deque

n = int(input())
petrol_pumps = deque([[int(x) for x in input().split()] for _ in range(n)])

pumps_copy = petrol_pumps.copy()
fuel, idx = 0, 0
while pumps_copy:
    amount, distance = pumps_copy.popleft()
    fuel += (amount - distance)
    if fuel < 0:
        petrol_pumps.rotate(-1)
        pumps_copy = petrol_pumps.copy()
        fuel = 0
        idx += 1
else:
    print(idx)
