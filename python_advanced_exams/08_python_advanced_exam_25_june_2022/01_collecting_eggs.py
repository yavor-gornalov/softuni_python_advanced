# https://judge.softuni.org/Contests/Practice/Index/3515#0

from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
pieces_of_paper = deque([int(x) for x in input().split(", ")])

boxes = 0
while eggs and pieces_of_paper:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == 13:
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue

    current_paper = pieces_of_paper.pop()

    if current_egg + current_paper <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

print(f"Eggs left: {', '.join(str(x) for x in eggs)}") if eggs else None
print(f"Pieces of paper left: {', '.join(str(x) for x in pieces_of_paper)}") if pieces_of_paper else None
