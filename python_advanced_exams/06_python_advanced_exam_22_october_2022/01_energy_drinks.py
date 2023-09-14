# https://judge.softuni.org/Contests/Practice/Index/3596#0

from collections import deque

caffeine_milligrams = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])

MAX_CAFFEINE = 300
total_caffeine = 0
while caffeine_milligrams and energy_drinks:
    milligrams = caffeine_milligrams.pop()
    dose = energy_drinks.popleft()
    current_caffeine = milligrams * dose

    if total_caffeine + current_caffeine <= MAX_CAFFEINE:
        total_caffeine += current_caffeine
        continue

    energy_drinks.append(dose)
    total_caffeine = max(0, total_caffeine - 30)

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
