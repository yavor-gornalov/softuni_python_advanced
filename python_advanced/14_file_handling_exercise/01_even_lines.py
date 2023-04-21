"""
Write a program that reads a text file and prints on the console its even lines.
Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@"
and reverse the order of the words.
"""

symbols = {"-", ",", ".", "!", "?"}
new_symbol = "@"

text_file_path = "./files/text.txt"
with open(text_file_path, "w") as file:
    file.write(
        "-I was quick to judge him, but it wasn't his fault.\n"
        "-Is this some kind of joke?! Is it?\n"
        "-Quick, hide here. It is safer."
    )

with open(text_file_path, "r") as file:
    text = file.readlines()

result = []
for i in range(0, len(text), 2):
    for symbol in symbols:
        text[i] = text[i].replace(symbol, new_symbol)
    print(" ".join(text[i].split()[::-1]))
