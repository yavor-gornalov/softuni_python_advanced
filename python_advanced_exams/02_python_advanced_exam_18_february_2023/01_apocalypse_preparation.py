# https://judge.softuni.org/Contests/Practice/Index/3889#0

from collections import deque

healing_items = {
    "Patch": [30, 0],
    "Bandage": [40, 0],
    "MedKit": [100, 0],
}

textiles = deque([int(x) for x in input().split()])
medics = deque([int(x) for x in input().split()])

while textiles and medics:
    textile = textiles.popleft()
    medicament = medics.pop()
    check_sum = textile + medicament

    created = False
    for item, item_data in healing_items.items():
        if check_sum == item_data[0]:
            item_data[1] += 1
            created = True
            break
    if created:
        continue

    if check_sum > healing_items["MedKit"][0]:
        medics[-1] += check_sum - healing_items["MedKit"][0]
        healing_items["MedKit"][1] += 1
        continue

    medics.append(medicament + 10)

if not textiles and not medics:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

for el, data in sorted(healing_items.items(), key=lambda x: (-x[1][1], x[0])):
    print(f"{el} - {data[1]}") if data[1] > 0 else None

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
if medics:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medics)])}")
