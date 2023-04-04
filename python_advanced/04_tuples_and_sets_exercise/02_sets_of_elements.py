# https://judge.softuni.org/Contests/Practice/Index/1833#1

n, m = (map(int, input().split()))
n_set = {int(input()) for _ in range(n)}
m_set = {int(input()) for _ in range(m)}

print(*m_set.intersection(n_set), sep="\n")
