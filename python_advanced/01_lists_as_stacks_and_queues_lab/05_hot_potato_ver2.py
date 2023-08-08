# https://judge.softuni.org/Contests/Practice/Index/1830#4
# Example from Mario Zahariev
from collections import deque

circle = deque(input().split())
step = int(input())

while len(circle) > 1:
    for _ in range(step - 1):
        circle.append(circle.popleft())
    print(f"Removed {circle.popleft()}")
print(f"Last is {circle.popleft()}")
