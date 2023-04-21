"""
Create a program that deletes the file 'files/my_first_file.txt' you have already created.
If you try to delete the file multiple times, print the message: 'File already deleted!'.
"""

import os

file_path = "./files/my_first_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')
