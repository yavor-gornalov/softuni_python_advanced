from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches_count = 0
while males and females:
    first_female = females.popleft()
    last_male = males.pop()

    if first_female <= 0 and last_male <= 0:
        continue
    if first_female <= 0:
        males.append(last_male)
        continue
    if last_male <= 0:
        females.appendleft(first_female)
        continue

    if first_female % 25 == 0:
        if females:
            first_female = females.popleft()
            males.append(last_male)
            continue
        else:
            break

    if last_male % 25 == 0:
        if males:
            last_male = males.pop()
            females.appendleft(first_female)
            continue
        else:
            break

    if first_female != last_male:
        males.append(last_male - 2)
        continue

    matches_count += 1

result = [f"Matches: {matches_count}",
          f"Males left: {', '.join([str(m) for m in reversed(males)])}" if males else "Males left: none",
          f"Females left: {', '.join([str(f) for f in females])}" if females else "Females left: none"]

print('\n'.join(result))
