# https://judge.softuni.org/Contests/Practice/Index/1831#1

from collections import deque

stack = deque()
commands = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None
}

n = int(input())
for _ in range(n):
    command = [int(x) for x in input().split()]
    commands[command[0]](command)

stack.reverse()
print(*stack, sep=", ")
