# https://judge.softuni.org/Contests/Practice/Index/1833#3

text = tuple(input())
uniques = {x for x in text}

[print(f"{el}: {text.count(el)} time/s") for el in sorted(uniques)]
