# https://judge.softuni.org/Contests/Practice/Index/1831#5

from collections import deque

text = input()

elements = [["{", "}"], ["[", "]"], ("(", ")")]

text_copy = text
balanced = True
for el in elements:
    parentheses = deque()
    index = 0
    while index < len(text_copy):
        if el[0] not in text_copy and el[1] not in text_copy:
            break
        if text_copy[index] == el[0]:
            parentheses.append(index)
        elif text_copy[index] == el[1]:
            if not parentheses:
                balanced = False
                break
            start_index = parentheses.pop()
            if len(text_copy[start_index:index + 1]) % 2 > 0:
                balanced = False
                break
        index += 1
    for ch in el:
        text = text.replace(ch, "")
    text_copy = text

print("YES") if balanced else print("NO")
