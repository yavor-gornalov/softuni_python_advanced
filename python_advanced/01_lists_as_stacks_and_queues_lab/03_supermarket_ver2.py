# https://judge.softuni.org/Contests/Practice/Index/1830#2

from collections import deque


def empty_queue(queue):
    while queue:
        print(queue.popleft())
    return True


def count_remaining(queue):
    print(f"{len(queue)} people remaining.")
    return False


commands = {
    "Paid": empty_queue,
    "End": count_remaining
}

queue = deque()
while True:
    line = input()
    if line not in commands:
        queue.append(line)
        continue
    if not commands[line](queue):
        break
