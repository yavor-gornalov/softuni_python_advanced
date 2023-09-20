n, m = [int(x) for x in input().split()]

first = set()
second = set()
[first.add(input()) for _ in range(n)]
[second.add(input()) for _ in range(m)]
unique_elements = first.intersection(second)

print('\n'.join(unique_elements))
