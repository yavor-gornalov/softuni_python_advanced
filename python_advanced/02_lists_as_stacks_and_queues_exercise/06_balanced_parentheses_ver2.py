# https://judge.softuni.org/Contests/Practice/Index/1831#5

from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    p = parentheses.popleft()
    if p in "{[(":
        open_parentheses.append(p)
    elif not open_parentheses:
        print("NO")
        break
    else:
        combination = open_parentheses.pop() + p
        if combination not in "(){}[]":
            print("NO")
            break
else:
    print("YES")
