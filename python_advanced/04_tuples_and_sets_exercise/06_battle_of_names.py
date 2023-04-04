# https://judge.softuni.org/Contests/Practice/Index/1833#5

odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    points = sum([ord(x) for x in input()]) // i
    if points % 2:
        odd_set.add(points)
    else:
        even_set.add(points)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
