from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}
crafted_presents = {}

while materials and magic:
    last_material = materials.pop()
    first_magic = magic.popleft()
    product = last_material * first_magic

    if product in presents.values():
        present = None
        for p, v in presents.items():
            if v == product:
                present = p
                break
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1
    elif product < 0:
        materials.append(first_magic + last_material)
        # for m in materials:
        #     m += first_magic + last_material
    elif product > 0:
        materials.append(last_material + 15)
    elif product == 0:
        materials.append(last_material) if last_material else None
        magic.appendleft(first_magic) if first_magic else None

merry_christmas = False
if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
        ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    merry_christmas = True

print("The presents are crafted! Merry Christmas!") if merry_christmas else print("No presents this Christmas!")
print(f"Materials left: {', '.join([str(m) for m in reversed(materials)])}") if materials else None
print(f"Magic left: {', '.join([str(m) for m in magic])}") if magic else None
for toy_name, amount in sorted(crafted_presents.items()):
    print(f"{toy_name}: {amount}")
