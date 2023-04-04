# https://judge.softuni.org/Contests/Practice/Index/1833#4

max_intersection = []
for _ in range(int(input())):
    first_range, second_range = [list(map(int, r.split(","))) for r in input().split("-")]
    first_set = set(range(first_range[0], first_range[1] + 1))
    second_set = set(range(second_range[0], second_range[1] + 1))
    if len(first_set.intersection(second_set)) > len(max_intersection):
        max_intersection = first_set.intersection(second_set)

print(f"Longest intersection is [{', '.join([str(x) for x in max_intersection])}] with length {len(max_intersection)}")
