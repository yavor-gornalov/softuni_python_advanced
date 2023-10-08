import os


def get_files_recursive(path, collection):
    file_list = os.listdir(path)
    for filename in file_list:
        file = os.path.join(path, filename)
        if os.path.isfile(file):
            extension = filename.split(".")[-1]
            if extension not in collection:
                collection[extension] = []
            collection[extension].append(filename)
        elif os.path.isdir(file):
            get_files_recursive(os.path.join(path, filename), collection)

    return collection


# main
while True:
    folder_path = input("Enter folder path: ")
    if os.path.exists(folder_path):
        break
    print("Please enter valid path!")

files_by_extension = {}
get_files_recursive(folder_path, files_by_extension)

sorted_files = {k: sorted(v) for k, v in sorted(files_by_extension.items())}

result = []
for ext, files in sorted_files.items():
    result.append(f"{ext}")
    for f_name in files:
        result.append(f"- - - {f_name}")

report_directory = "files"
os.makedirs(report_directory, exist_ok=True)
report_file_name = "report.txt"
report_path = os.path.join(report_directory, report_file_name)
with open(report_path, "w") as report:
    report.write('\n'.join(result))
print(f'Report finished! File "{report_path}" - created!')
