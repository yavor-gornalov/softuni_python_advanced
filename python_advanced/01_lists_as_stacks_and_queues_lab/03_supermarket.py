# https://judge.softuni.org/Contests/Practice/Index/1830#2

from collections import deque

queue = deque([])

while True:
    name = input()
    if name == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif name == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(name)
