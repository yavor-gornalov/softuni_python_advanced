def read_next(*args):
    for arg in args:
        yield from arg


def read_next_old(*args):
    iterable = []
    [iterable.extend(a) for a in args]
    idx = 0
    while idx < len(iterable):
        yield iterable[idx]
        idx += 1


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)
