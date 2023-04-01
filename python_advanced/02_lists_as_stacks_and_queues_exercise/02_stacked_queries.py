# https://judge.softuni.org/Contests/Practice/Index/1831#1

stack = []
n = int(input())

for _ in range(n):
    command = input()
    if command.startswith("1"):
        num = command.split()[1]
        stack.append(num)
    elif command.startswith("2"):
        stack.pop() if stack else 0
    elif command.startswith("3"):
        print(max(stack)) if stack else 0
    elif command.startswith("4"):
        print(min(stack)) if stack else 0

while len(stack) > 1:
    print(stack.pop(), end=", ")
print(stack.pop())
