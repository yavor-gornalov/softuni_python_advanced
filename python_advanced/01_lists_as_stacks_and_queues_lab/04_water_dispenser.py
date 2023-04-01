# https://judge.softuni.org/Contests/Practice/Index/1830#3

from collections import deque

queue = deque()

liters_left = int(input())
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        quantity = int(command.split(" ")[1])
        liters_left += quantity
        continue
    quantity = int(command)
    name = queue.popleft()
    if liters_left >= quantity:
        liters_left -= quantity
        print(f"{name} got water")
    else:
        print(f"{name} must wait")

print(f"{liters_left} liters left")
