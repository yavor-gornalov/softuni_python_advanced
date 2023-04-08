# https://judge.softuni.org/Contests/Practice/Index/1835#4

def letter_offset(letter, offset):
    return chr(ord(letter) + offset)


rows, cols = [int(x) for x in input().split()]

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        first_last = letter_offset('a', i)
        middle = letter_offset('a', i + j)
        row.append(first_last + middle + first_last)
    print(*row, sep=" ")
