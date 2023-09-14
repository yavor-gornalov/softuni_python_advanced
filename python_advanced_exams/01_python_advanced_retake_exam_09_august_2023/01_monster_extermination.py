# https://judge.softuni.org/Contests/Practice/Index/4089#0

from collections import deque

armor_values = deque([int(x) for x in input().split(",")])
impact_values = deque([int(x) for x in input().split(",")])

killed_monsters = 0
while armor_values and impact_values:
    monster_armor = armor_values.popleft()
    solder_strike = impact_values.pop()
    if solder_strike >= monster_armor:
        killed_monsters += 1
        solder_strike -= monster_armor
        if solder_strike:
            if impact_values:
                impact_values[-1] += solder_strike
            else:
                impact_values.append(solder_strike)
    else:
        monster_armor -= solder_strike
        armor_values.append(monster_armor)

if not armor_values:
    print("All monsters have been killed!")
if not impact_values:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
