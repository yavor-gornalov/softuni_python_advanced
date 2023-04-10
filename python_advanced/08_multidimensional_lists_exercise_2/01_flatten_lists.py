# https://judge.softuni.org/Contests/Practice/Index/3194#0

array = [[int(x.strip()) for x in nums.split()] for nums in input().split("|")]

numbers = [ele for sub_array in reversed(array) for ele in sub_array]
print(*numbers, sep=" ")
