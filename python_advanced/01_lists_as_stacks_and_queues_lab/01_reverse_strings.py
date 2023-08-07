# https://judge.softuni.org/Contests/Practice/Index/1830#0

text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))
