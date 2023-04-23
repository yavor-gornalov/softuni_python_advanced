import os

files_by_extensions = {}


def save_file_extensions(path, extensions):
    file_list = os.listdir(path)
    for filename in file_list:
        file = os.path.join(path, filename)
        if os.path.isfile(file):
            extension = filename.split(".")[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)
        elif os.path.isdir(file):
            save_file_extensions(os.path.join(path, filename), extensions)

    return extensions


# main
folder_path = input("Enter folder path:")
while not os.path.exists(folder_path):
    print("Please enter valid path!")
    folder_path = input("Enter folder path:")

save_file_extensions(folder_path, files_by_extensions)

sorted_extensions = {k: sorted(v) for k, v in sorted(files_by_extensions.items())}

result = ""
for ext, files in sorted_extensions.items():
    result += f"{ext}\n"
    for f in files:
        result += f"- - - {f}\n"

print(result)
report_path = "./files/report.txt"
with open(report_path, "w") as report:
    report.write(result)
