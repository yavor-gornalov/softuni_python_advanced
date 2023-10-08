"""
Write a program that reads a text file, inserts line numbers in front of each line,
and counts all the letters and punctuation marks.
The result should be written to another text file.
"""

import os
from string import punctuation

output_directory = "files"
os.makedirs(output_directory, exist_ok=True)

text_file_path = os.path.join(output_directory, "text.txt")
output_file_path = os.path.join(output_directory, "output.txt")

# recreate text.txt
with open(text_file_path, "w") as file:
    file.write("""-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.""")

with open(text_file_path, "r") as file:
    text = file.readlines()

output = []
for line_number, line in enumerate(text, 1):
    letters, punctuation_marks = 0, 0
    for symbol in line:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punctuation_marks += 1

    output.append(f"Line {line_number}: {line.strip()} ({letters})({punctuation_marks})\n")

with open(output_file_path, "w") as file:
    file.writelines(output)
print(f'File "{output_file_path}" - created!')
