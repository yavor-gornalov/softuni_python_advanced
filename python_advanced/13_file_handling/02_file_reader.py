"""
You are given a file called files/numbers.txt
Create a program that reads the numbers from the file.
Print on the console the sum of those numbers.
"""

total = 0
with open("./files/numbers.txt", "r") as file:
    for line in file:
        num = int(line)
        total += num
        print(num)

print(f"Sum: {total}")
a
