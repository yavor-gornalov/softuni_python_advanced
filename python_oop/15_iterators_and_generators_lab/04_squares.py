def squares(n):
    i = 0
    while i < n:
        i += 1
        yield i ** 2


print(list(squares(5)))
