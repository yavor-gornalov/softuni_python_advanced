# https://judge.softuni.org/Contests/Practice/Index/3159#2

from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups = deque([int(x) for x in input().split(", ")])

shakes_count = 0
while chocolates and cups and shakes_count < 5:
    chocolate = chocolates.pop()
    cup = cups.popleft()

    if cup <= 0 and chocolate <= 0:
        continue
    elif cup <= 0:
        chocolates.append(chocolate)
        continue
    elif chocolate <= 0:
        cups.appendleft(cup)
        continue

    if cup == chocolate:
        shakes_count += 1
        continue

    cups.append(cup)
    chocolates.append(chocolate - 5)

print("Great! You made all the chocolate milkshakes needed!") if shakes_count >= 5 else print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(ch) for ch in chocolates)}") if chocolates else print("Chocolate: empty")

print(f"Milk: {', '.join(str(c) for c in cups)}") if cups else print("Milk: empty")
