"""
Write a program that reads a text file and prints on the console its even lines.
Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@"
and reverse the order of the words.
"""
import os

output_directory = "files"
os.makedirs(output_directory, exist_ok=True)
text_file_name = "text.txt"
text_file_path = os.path.join(output_directory, text_file_name)

symbols = {"-", ",", ".", "!", "?"}
new_symbol = "@"

with open(text_file_path, "w") as file:
    file.write("""-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.""")

with open(text_file_path, "r") as file:
    text = file.readlines()

for line_idx in range(0, len(text), 2):
    for symbol in symbols:
        text[line_idx] = text[line_idx].replace(symbol, new_symbol)
    print(" ".join(text[line_idx].split()[::-1]))
