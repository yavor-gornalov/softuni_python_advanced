# # https://judge.softuni.org/Contests/Practice/Index/3159#5

from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
color_combos = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

color_parts = input().split()

formed_colors = []
formed_secondary_colors = []
while color_parts:
    first_part = color_parts.pop(0)
    last_part = color_parts.pop() if color_parts else ""

    current_combinations = {first_part + last_part, last_part + first_part}
    formed_color = current_combinations.intersection(main_colors.union(secondary_colors))
    color = [x for x in formed_color][0] if formed_color else None

    if color:
        formed_colors.append(color)
        if color in secondary_colors:
            formed_secondary_colors.append(color)

    else:
        first_part = first_part[:-1]
        color_parts.insert(len(color_parts) // 2, first_part) if first_part else None
        last_part = last_part[:-1]
        color_parts.insert(len(color_parts) // 2, last_part) if last_part else None

for col in formed_secondary_colors:
    if color_combos[col][0] not in formed_colors or color_combos[col][1] not in formed_colors:
        formed_colors.remove(col)

print(formed_colors)
