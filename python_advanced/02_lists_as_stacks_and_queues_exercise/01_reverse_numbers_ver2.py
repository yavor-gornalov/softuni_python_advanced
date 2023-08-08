# https://judge.softuni.org/Contests/Practice/Index/1831#0

from collections import deque

stack = deque(input().split())

stack.reverse()
print(*stack, sep=" ")
