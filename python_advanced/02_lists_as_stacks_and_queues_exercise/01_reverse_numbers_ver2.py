# https://judge.softuni.org/Contests/Practice/Index/1831#0

from collections import deque

stack = deque()
[stack.append(int(x)) for x in input().split()]

stack.reverse()
print(*stack, sep=" ")
