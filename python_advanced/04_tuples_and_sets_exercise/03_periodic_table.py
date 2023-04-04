# https://judge.softuni.org/Contests/Practice/Index/1833#2

n = int(input())
unique_elements = set()
for _ in range(n):
    [unique_elements.add(el) for el in input().split()]

# unique_elements = {el for _ in range(n) for el in input().split()}

print(*unique_elements, sep="\n")
