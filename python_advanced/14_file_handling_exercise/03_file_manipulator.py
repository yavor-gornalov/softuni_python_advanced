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
    open(f_name, "w").close()


def append_to_file(f_name, f_content):
    with open(f_name, "a") as file:
        file.writelines(f_content + "\n")


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


ACTIONS = {
    "Create": create_file,
    "Add": append_to_file,
    "Replace": replace_text,
    "Delete": delete_file
}

output_directory = "./files"
os.makedirs(output_directory, exist_ok=True)
while True:
    command = input()
    if command == "End":
        break
    action, filename, *args = command.split("-")
    filename = os.path.join(output_directory, filename)
    if action not in ACTIONS:
        continue
    ACTIONS[action](filename, *args)

"""
TEST COMMANDS:
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
"""