# https://judge.softuni.org/Contests/Practice/Index/1830#1

text = input()

parentheses = []
for index in range(len(text)):
    if text[index] == "(":
        parentheses.append(index)
    elif text[index] == ")":
        start_index = parentheses.pop()
        print(text[start_index:index + 1])
