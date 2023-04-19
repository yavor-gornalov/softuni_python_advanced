# https://judge.softuni.org/Contests/Practice/Index/1839#10

from collections import deque


def math_operations(*args, **kwargs):
    operations = {
        "a": lambda x, y: x + y,
        "s": lambda x, y: x - y,
        "d": lambda x, y: x / y if y != 0 else x,
        "m": lambda x, y: x * y,
    }

    commands = deque("asdm")
    for arg in args:
        operator = commands.popleft()
        kwargs[operator] = operations[operator](kwargs[operator], arg)
        commands.append(operator)

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = "\n".join([f"{key}: {value:.1f}" for key, value in sorted_kwargs])

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, s=7, d=33, m=15, a=1))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
