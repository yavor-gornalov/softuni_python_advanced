def words_sorting(*args):
    words = {arg: sum([ord(c) for c in arg]) for arg in args}
    if sum(words.values()) % 2 == 0:
        return '\n'.join(f"{k} - {v}" for (k, v) in sorted(words.items(), key=lambda x: x[0]))
    return '\n'.join(f"{k} - {v}" for (k, v) in sorted(words.items(), key=lambda x: -x[1]))


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
