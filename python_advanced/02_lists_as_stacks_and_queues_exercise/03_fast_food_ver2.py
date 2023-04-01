# https://judge.softuni.org/Contests/Practice/Index/1831#2

from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders)) if orders else None
for order in orders.copy():
    if order > quantity:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
    orders.popleft()
    quantity -= order
else:
    print("Orders complete")
