# https://judge.softuni.org/Contests/Practice/Index/1832#2

names = [input() for _ in range(int(input()))]
uniques = set(names)

[print(name) for name in uniques]
