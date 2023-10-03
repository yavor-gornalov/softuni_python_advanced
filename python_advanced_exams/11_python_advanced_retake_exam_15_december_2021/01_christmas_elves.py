from collections import deque

elves = deque(int(x) for x in input().split())
boxes = deque(int(x) for x in input().split())

turn = 0
total_energy_used = 0
total_toys_crafted = 0
while elves and boxes:
    elf = elves.popleft()
    box = boxes.pop()

    if elf < 5:
        boxes.append(box)
        continue

    turn += 1

    if turn % (3 * 5) == 0:
        if elf >= 2 * box:
            total_energy_used += 2 * box
            elf -= 2 * box
            elves.append(elf)
            continue

    elif turn % 3 == 0:
        if elf >= 2 * box:
            total_toys_crafted += 2
            elf -= 2 * box
            total_energy_used += 2 * box
            elves.append(elf + 1)
            continue

    elif turn % 5 == 0:
        if elf >= box:
            total_energy_used += box
            elf -= box
            elves.append(elf)
            continue

    else:
        if elf >= box:
            total_toys_crafted += 1
            elf -= box
            total_energy_used += box
            elves.append(elf + 1)
            continue

    elves.append(2 * elf)
    boxes.append(box)

print(f"Toys: {total_toys_crafted}")
print(f"Energy: {total_energy_used}")
print(f"Elves left: {', '.join([str(e) for e in elves])}") if elves else None
print(f"Boxes left: {', '.join([str(b) for b in boxes])}") if boxes else None
