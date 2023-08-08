# https://judge.softuni.org/Contests/Practice/Index/1831#4

from collections import deque

petrol_pumps = deque()
pumps_count = int(input())

for idx in range(pumps_count):
    petrol_pumps.append([idx] + [int(x) for x in input().split()])

total_fuel = counter = 0
while True:
    if counter == len(petrol_pumps):
        print(petrol_pumps[0][0])
        break

    idx, current_fuel, current_distance = petrol_pumps[0]
    total_fuel += current_fuel - current_distance

    petrol_pumps.rotate(-1)

    if total_fuel < 0:
        total_fuel = counter = 0
    else:
        counter += 1


