n = int(input())
unique_elements = set()

[[unique_elements.add(el) for el in input().split()] for _ in range(n)]

print('\n'.join(unique_elements))
