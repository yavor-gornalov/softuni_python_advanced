# https://judge.softuni.org/Contests/Practice/Index/1830#4

from collections import deque

queue = deque(input().split())
n = int(input())

counter = 1
while len(queue) > 1:
    kid = queue.popleft()
    if not counter % n:
        print(f"Removed {kid}")
    else:
        queue.append(kid)
    counter += 1
print(f"Last is {queue.popleft()}")
