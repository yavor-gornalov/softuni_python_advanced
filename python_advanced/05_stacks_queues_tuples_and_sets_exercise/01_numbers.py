# https://judge.softuni.org/Contests/Practice/Index/3159#0

from collections import deque

first_seq = {int(x) for x in input().split()}
second_seq = {int(x) for x in input().split()}

for _ in range(int(input())):
    command_line = deque(input().split())
    command, sequence = [command_line.popleft() for _ in range(2)]
    if command == "Add":
        if sequence == "First":
            [first_seq.add(int(x)) for x in command_line]
        elif sequence == "Second":
            [second_seq.add(int(x)) for x in command_line]
    elif command == "Remove":
        if sequence == "First":
            [first_seq.remove(int(x)) for x in command_line if int(x) in first_seq]
        elif sequence == "Second":
            [second_seq.remove(int(x)) for x in command_line if int(x) in second_seq]
    else:
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(*sorted(first_seq), sep=", ")
print(*sorted(second_seq), sep=", ")
