def genrange(current_idx, end):
    while current_idx <= end:
        yield current_idx
        current_idx += 1


print(list(genrange(1, 10)))
