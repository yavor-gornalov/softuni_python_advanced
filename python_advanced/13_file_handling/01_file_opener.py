"""
You are given a file called files/text.txt
Create a program that opens the file. If the file is found, print 'File found'.
If the file is not found, print 'File not found'
"""

try:
    file = open("./files/text.txt", "r")
    print('File found')
    # not included in the exercise
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found")
