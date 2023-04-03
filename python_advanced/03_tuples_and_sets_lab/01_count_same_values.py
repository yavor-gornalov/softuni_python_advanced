# https://judge.softuni.org/Contests/Practice/Index/1832#0

nums = tuple([float(x) for x in input().split()])

uniques = {}
for num in nums:
    if num not in uniques:
        uniques[num] = nums.count(num)

[print(f"{num:.1f} - {cnt} times") for num, cnt in uniques.items()]
