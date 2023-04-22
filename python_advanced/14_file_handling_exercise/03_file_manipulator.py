"""
Create a program that will receive commands until the command "End". The commands can be:
    • "Create-{file_name}" - Creates the given file with an empty content.
    If the file already exists, remove the existing text in it (as if the file is created again)
    • "Add-{file_name}-{content}" - Append the content and a new line after it.
    If the file does not exist, create it, and add the content
    • "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences
    of the old string with the new string. If the file does not exist, print: "An error occurred"
    • "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
"""
import os.path


def create_file(f_name):
    with open(f_name, "w"):
        pass


def append_to_file(f_name, cont):
    with open(f_name, "a") as file:
        file.writelines(cont + "\n")


def replace_text(f_name, old_str, new_str):
    if os.path.exists(f_name):
        with open(f_name, "r") as file:
            text = file.read()

        text = text.replace(old_str, new_str)

        with open(f_name, "w") as file:
            file.write(text)

    else:
        print("Replace: An error occurred")


def delete_file(f_name):
    if os.path.exists(f_name):
        os.remove(f_name)
    else:
        print("Delete: An error occurred")


while True:
    command = input()
    if command == "End":
        break

    action, filename, *args = command.split("-")
    filename = "./files/" + filename
    if action == "Create":
        create_file(filename)
    elif action == "Add":
        append_to_file(filename, *args)
    elif action == "Replace":
        replace_text(filename, *args)
    elif action == "Delete":
        delete_file(filename)
