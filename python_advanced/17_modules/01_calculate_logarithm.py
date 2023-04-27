from math import log, e as exponent


def calculate_logarithm(number, log_base):
    if log_base.lower() == "natural":
        return log(num, exponent)
    return log(number, int(log_base))


num = int(input())
base = input()

result = calculate_logarithm(num, base)
print(f"{result:.2f}")
