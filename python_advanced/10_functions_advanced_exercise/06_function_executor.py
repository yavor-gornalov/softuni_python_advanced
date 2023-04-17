# https://judge.softuni.org/Contests/Practice/Index/1839#5

def func_executor(*args):
    result = ""
    for arg in args:
        func, params = arg
        result += f"{func.__name__} - {func(*params)}\n"
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
