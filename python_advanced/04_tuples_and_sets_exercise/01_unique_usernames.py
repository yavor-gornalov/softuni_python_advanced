# https://judge.softuni.org/Contests/Practice/Index/1833#0

n = int(input())
uniques = {input() for _ in range(n)}

print(*uniques, sep='\n')
