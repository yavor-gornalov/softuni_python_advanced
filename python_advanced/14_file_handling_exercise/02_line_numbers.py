"""
Write a program that reads a text file, inserts line numbers in front of each line,
and counts all the letters and punctuation marks.
The result should be written to another text file.
"""

from string import punctuation

text_file_path = "./files/text.txt"
output_file_path = "./files/output.txt"

with open(text_file_path, "r") as file:
    text = file.readlines()

output = []
letters, punctuation_marks = 0, 0
for line_number, line in enumerate(text, 1):
    for symbol in line:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punctuation_marks += 1

    output.append(f"Line {line_number}: {line.strip()} ({letters})({punctuation_marks})\n")

with open(output_file_path, "w")as file:
    file.writelines(output)
