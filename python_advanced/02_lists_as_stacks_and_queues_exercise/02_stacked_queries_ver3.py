# https://judge.softuni.org/Contests/Practice/Index/1831#1

from collections import deque

stack = deque()

commands = {
    1: lambda x: stack.append(x),
    2: lambda: stack.pop() if stack else None,
    3: lambda: print(max(stack)) if stack else None,
    4: lambda: print(min(stack)) if stack else None
}

count = int(input())
for _ in range(count):
    command, *args = [int(x) for x in input().split()]
    commands[command](*args)

print(*reversed(stack), sep=", ")
