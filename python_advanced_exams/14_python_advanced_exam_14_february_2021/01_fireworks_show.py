from collections import deque

effects = deque(int(x) for x in input().split(", "))
explosives = deque(int(x) for x in input().split(", "))

fireworks_amounts = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}

preparation_finished = False
while effects and explosives and not preparation_finished:
    effect = effects.popleft()
    explosive = explosives.pop()

    if effect <= 0 and explosive <= 0:
        continue
    elif effect <= 0:
        explosives.append(explosive)
        continue
    elif explosive <= 0:
        effects.appendleft(effect)
        continue

    mix_value = effect + explosive
    if mix_value % 3 == 0 and mix_value % 5 != 0:
        fireworks_amounts["Palm"] += 1
    elif mix_value % 3 != 0 and mix_value % 5 == 0:
        fireworks_amounts["Willow"] += 1
    elif mix_value % 3 == 0 and mix_value % 5 == 0:
        fireworks_amounts["Crossette"] += 1
    else:
        effects.append(effect - 1)
        explosives.append(explosive)
    preparation_finished = all(x >= 3 for x in fireworks_amounts.values())

result = []
if preparation_finished:
    result.append("Congrats! You made the perfect firework show!")
else:
    result.append("Sorry. You can't make the perfect firework show.")
result.append(f"Firework Effects left: {', '.join([str(x) for x in effects])}") if effects else None
result.append(f"Explosive Power left: {', '.join([str(x) for x in explosives])}") if explosives else None
[result.append(f"{key} Fireworks: {amount}") for key, amount in fireworks_amounts.items()]

print(*result, sep='\n')
