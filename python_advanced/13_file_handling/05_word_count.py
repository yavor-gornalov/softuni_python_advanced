"""
Write a program that reads a list of words from the file ./files/words.txt
and finds how many times each of the words is contained in another file ./files/text.txt.
Matching should be case-insensitive.
The results should be written to other text files.
Sort the words by frequency in descending order.
"""
import re

with open("./files/words.txt", "r") as words_file:
    key_words = words_file.read().split()

words_count = dict.fromkeys(key_words, 0)

with open("./files/input.txt", "r") as input_file:
    text = input_file.read()
    for key in key_words:
        words_count[key] = len(re.findall(rf"\b{key.lower()}+\b", text.lower()))

sorted_result = sorted(words_count.items(), key=lambda x: -x[1])
output = "\n".join([f"{w} - {c}" for w, c in sorted_result])

with open("./files/output.txt", "w") as output_file:
    output_file.write(output)
