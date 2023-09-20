n = int(input())
unique_usernames = set()
[unique_usernames.add(input()) for _ in range(n)]
print('\n'.join(unique_usernames))
