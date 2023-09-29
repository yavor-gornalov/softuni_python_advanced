from functools import reduce


def sum_numbers(*args):
    return sum(args)


def multiply_numbers(*args):
    return reduce(lambda x, y: x * y, args)


def func_executor(*args):
    result = []
    for func, nums in args:
        result.append(f"{func.__name__} - {func(*nums)}")
    return "\n".join(result)


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
