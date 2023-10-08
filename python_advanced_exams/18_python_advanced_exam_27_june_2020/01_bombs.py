from collections import deque

bomb_types = {
    40: ["Datura", 0],
    60: ["Cherry", 0],
    120: ["Smoke Decoy", 0]
}

effects = deque(int(x) for x in input().split(", "))
casings = deque(int(x) for x in input().split(", "))

bombs_prepared = False
while effects and casings and not bombs_prepared:
    effect = effects[0]
    casing = casings[-1]

    bomb = effect + casing
    if bomb not in bomb_types:
        casings[-1] -= 5
        continue

    bomb_types[bomb][1] += 1
    effects.popleft()
    casings.pop()
    bombs_prepared = all(x[1] >= 3 for x in bomb_types.values())
result = []
if bombs_prepared:
    result.append("Bene! You have successfully filled the bomb pouch!")
else:
    result.append("You don't have enough materials to fill the bomb pouch.")
if not effects:
    result.append("Bomb Effects: empty")
else:
    result.append(f"Bomb Effects: {', '.join([str(e) for e in effects])}")
if not casings:
    result.append("Bomb Casings: empty")
else:
    result.append(f"Bomb Casings: {', '.join([str(c) for c in casings])}")
for key, (bomb_type, amount) in sorted(bomb_types.items(), key=lambda x: x[1][0]):
    result.append(f"{bomb_type} Bombs: {amount}")

print(*result, sep='\n')
