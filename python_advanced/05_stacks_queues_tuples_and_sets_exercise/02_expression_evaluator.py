# https://judge.softuni.org/Contests/Practice/Index/3159#1

from collections import deque
from functools import reduce

nums_and_operators = deque(input().split())

current_list = deque()

el = 0
while nums_and_operators:
    el = nums_and_operators.popleft()
    if el in "*/+-":
        if el == "*":
            nums_and_operators.appendleft(str(reduce(lambda x, y: x * y, current_list)))
        elif el == "/":
            nums_and_operators.appendleft(str(reduce(lambda x, y: x // y, current_list)))
        elif el == "+":
            nums_and_operators.appendleft(str(reduce(lambda x, y: x + y, current_list)))
        elif el == "-":
            nums_and_operators.appendleft(str(reduce(lambda x, y: x - y, current_list)))
        current_list.clear()
    else:
        current_list.append(int(el))

print(el)
