from collections import deque


def craft_present(points):
    if points < 100:
        return "Low"
    elif points < 200:
        return "Gemstone"
    elif points < 300:
        return "Porcelain Sculpture"
    elif points < 400:
        return "Gold"
    elif points < 500:
        return "Diamond Jewellery"
    else:
        return "High"


materials = deque(int(x) for x in input().split())
magic_points = deque(int(x) for x in input().split())

presents_crafted = {}
while materials and magic_points:
    material = materials.pop()
    magic = magic_points.popleft()

    product = material + magic
    present = craft_present(product)
    if present == "Low":
        if product % 2 == 0:
            product = 2 * material + 3 * magic
        else:
            product *= 2
        present = craft_present(product)
    elif present == "High":
        product /= 2
        present = craft_present(product)

    if present in ["Low", "High"]:
        continue
    if present not in presents_crafted:
        presents_crafted[present] = 0
    presents_crafted[present] += 1

result = []
if "Gemstone" in presents_crafted and "Porcelain Sculpture" in presents_crafted \
        or "Gold" in presents_crafted and "Diamond Jewellery" in presents_crafted:
    result.append("The wedding presents are made!")
else:
    result.append("Aladdin does not have enough wedding presents.")

result.append(f"Materials left: {', '.join([str(x) for x in materials])}") if materials else None
result.append(f"Magic left: {', '.join([str(x) for x in magic_points])}") if magic_points else None
if presents_crafted:
    for present, amount in sorted(presents_crafted.items()):
        result.append(f"{present}: {amount}")

print(*result, sep='\n')
