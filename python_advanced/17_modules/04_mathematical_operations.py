from math_operations.basic_operations import calculation

args = input().split()
first_number = float(args[0])
operator = args[1]
second_number = int(args[2])

if operator not in "+-*/^":
    print("Operation not defined")
else:
    try:
        print(f"{calculation(operator, first_number, second_number):.2f}")
    except ZeroDivisionError:
        print("Division by zero is not allowed!")
