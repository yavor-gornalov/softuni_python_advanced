from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"],
}

formed_colors = []
formed_secondary_colors = []

queue = deque(input().split())
while queue:
    first = queue.popleft()
    last = queue.pop() if queue else ""

    if first + last in main_colors or first + last in secondary_colors:
        color = first + last
    elif last + first in main_colors or last + first in secondary_colors:
        color = last + first
    else:
        middle = len(queue) // 2
        first = first[:-1]
        last = last[:-1]
        queue.insert(middle, first) if first else None
        queue.insert(middle, last) if last else None
        continue

    formed_colors.append(color)
    if color in secondary_colors:
        formed_secondary_colors.append(color)

for secondary_color in formed_secondary_colors:
    main_colors_existing = True
    for c in secondary_colors[secondary_color]:
        if c not in formed_colors:
            main_colors_existing = False
            formed_colors.remove(secondary_color)
            break

print(formed_colors)
