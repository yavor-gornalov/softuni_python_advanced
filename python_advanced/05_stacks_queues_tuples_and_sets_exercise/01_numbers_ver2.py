commands = {
    "Add First": lambda x: first.update(x),
    "Add Second": lambda x: second.update(x),
    "Remove First": lambda x: first.difference_update(x),
    "Remove Second": lambda x: second.difference_update(x),
    "Check Subset": lambda x: first.issubset(second) or second.issubset(first)
}

first, second = [{int(x) for x in input().split()} for _ in range(2)]
is_subset = None

number_of_commands = int(input())
for _ in range(number_of_commands):
    data = input().split()
    command = " ".join(data[:2])
    numbers = {int(x) for x in data[2:]}
    if command not in commands:
        continue
    elif command.startswith("Check"):
        print(commands[command](numbers))
    else:
        commands[command](numbers)

print(f"{', '.join([str(x) for x in sorted(first)])}\n"
      f"{', '.join([str(x) for x in sorted(second)])}")
