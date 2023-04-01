# https://judge.softuni.org/Contests/Practice/Index/1831#4

from collections import deque

petrol_pumps = deque()

n = int(input())
for i in range(n):
    amount, distance = [int(x) for x in input().split()]
    pump = {"idx": i, "amount": amount, "distance": distance}
    petrol_pumps.append(pump)

for idx in range(n):
    pumps_copy = petrol_pumps.copy()
    fuel = 0
    while pumps_copy:
        current_pump = pumps_copy.popleft()
        fuel += (current_pump["amount"] - current_pump["distance"])
        if fuel < 0:
            break
    else:
        print(idx)
        break
    petrol_pumps.append(petrol_pumps.popleft())
