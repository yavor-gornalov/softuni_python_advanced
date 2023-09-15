# https://judge.softuni.org/Contests/Practice/Index/4081#0

from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance
    if result in challenges:
        idx = challenges.index(result)
        challenges.pop(idx)
        continue
    current_tool += 1
    tools.append(current_tool)
    current_substance -= 1
    substances.append(current_substance) if current_substance else None

if not all([tools, substances]) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(t) for t in tools])}")
if substances:
    print(f"Substances: {', '.join([str(s) for s in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")
