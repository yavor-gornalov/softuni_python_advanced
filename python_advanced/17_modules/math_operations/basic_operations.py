operations_mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b,
}


def calculation(operator, first_num, second_num):
    return operations_mapper[operator](first_num, second_num)
