# https://judge.softuni.org/Contests/Practice/Index/1831#5

from collections import deque

parentheses = deque(input())
opening_brackets = "{[("
solutions = "{}[]()"

buffer = []
balanced = True
while parentheses:
    bracket = parentheses.popleft()
    if bracket in opening_brackets:
        buffer.append(bracket)
    else:
        if not buffer:
            balanced = False
            break
        br = buffer.pop()
        if br + bracket not in solutions:
            balanced = False
            break

print("YES") if balanced and not buffer else print("NO")
