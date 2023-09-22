from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

number_of_shakes = 0
while chocolates and cups_of_milk and number_of_shakes < 5:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()
    if chocolate <= 0 and milk <= 0:
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if chocolate == milk:
        number_of_shakes += 1
        continue

    chocolate -= 5
    chocolates.append(chocolate)
    cups_of_milk.append(milk)

if number_of_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(ch) for ch in chocolates)}") if chocolates else print("Chocolate: empty")
print(f"Milk: {', '.join(str(m) for m in cups_of_milk)}") if cups_of_milk else print("Milk: empty")
