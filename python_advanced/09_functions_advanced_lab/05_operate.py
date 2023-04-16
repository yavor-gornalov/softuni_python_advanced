# https://judge.softuni.org/Contests/Practice/Index/1838#4

def operate(operator, *args):
    def add(*nums):
        return sum(nums)

    def subtract(x, *nums):
        return x + sum(-y for y in nums)

    def multiply(x, *nums):
        result = x
        for y in nums:
            result *= y
        return result

    def divide(x, *nums):
        result = x
        for y in nums:
            result /= y
        return result

    if operator == "+":
        return add(*args)
    elif operator == "-":
        return subtract(*args)
    elif operator == "*":
        return multiply(*args)
    elif operator == "/":
        return divide(*args)


print(operate("+", 1, 1, 1))
print(operate('-', 1, 2))
print(operate("*", 3, 4))
print(operate('/', 2, 2))
