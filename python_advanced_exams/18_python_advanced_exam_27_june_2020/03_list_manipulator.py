def list_manipulator(sequence, command, position, *args):
    if command == "add":
        if position == "beginning":
            sequence = list(args) + sequence
        elif position == "end":
            sequence.extend(args)
    elif command == "remove":
        count = args[0] if args else 1
        if position == "beginning":
            sequence = sequence[count:]
        elif position == "end":
            sequence = sequence[:-count]
    return sequence


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
