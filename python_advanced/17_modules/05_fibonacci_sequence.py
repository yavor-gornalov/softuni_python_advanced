from magic_sequences.fibonacci import create_fibonacci, get_fibonacci_index

command = input()
while command != "Stop":
    if command.startswith("Create"):
        count = int(command.split()[-1])
        result = create_fibonacci(count)
        print(*result, sep=" ")
    elif command.startswith("Locate"):
        number = int(command.split()[-1])
        result = get_fibonacci_index(number)
        if result:
            print(f"The number - {number} is at index {result}")
        else:
            print(f"The number {number} is not in the sequence")
    command = input()
