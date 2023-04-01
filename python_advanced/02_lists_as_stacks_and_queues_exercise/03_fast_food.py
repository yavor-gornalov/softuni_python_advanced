# https://judge.softuni.org/Contests/Practice/Index/1831#2

from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders)) if orders else None
while True:
    if not orders:
        print("Orders complete")
        break
    order_quantity = orders.popleft()
    if order_quantity > quantity:
        print(f"Orders left:", order_quantity, *orders, sep=" ")
        break
    quantity -= order_quantity
