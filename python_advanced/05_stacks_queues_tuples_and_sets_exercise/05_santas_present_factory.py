# https://judge.softuni.org/Contests/Practice/Index/3159#4

from collections import deque

material_boxes = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

presents = {
    "Doll": [150, 0],
    "Wooden train": [250, 0],
    "Teddy bear": [300, 0],
    "Bicycle": [400, 0]
}

while material_boxes and magic_levels:

    box = material_boxes.pop()
    magic = magic_levels.popleft()
    result = box * magic

    if result > 0:
        present_crafted = False
        for present, present_data in presents.items():
            if result == present_data[0]:
                present_data[1] += 1
                present_crafted = True
                break
        if present_crafted:
            continue
        material_boxes.append(box + 15)

    elif result < 0:
        material_boxes.append(box + magic)

    else:
        material_boxes.append(box) if box else None
        magic_levels.appendleft(magic) if magic else None

first_pair = presents["Doll"][1] and presents["Wooden train"][1]
second_pair = presents["Teddy bear"][1] and presents["Bicycle"][1]

if first_pair or second_pair:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

print(f"Materials left: {', '.join([str(x) for x in reversed(material_boxes)])}") if material_boxes else None
print(f"Magic left: {', '.join([str(x) for x in magic_levels])}") if magic_levels else None

for present, data in sorted(presents.items()):
    print(f"{present}: {data[1]}") if data[1] else None
