import os
# directory traversal
# tested with the "level_1" folder, this version of the task is without the "first level" limitation


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [filename]

        elif os.path.isdir(file):
            save_extensions(file)


directory = input("Enter the name of the directory: ")
extensions = {}
result = []

try:
    save_extensions(directory)

except FileNotFoundError:
    print("The directory is not found or doesn't exist!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("created_files/result.txt", "w") as result_file:
    result_file.write('\n'.join(result))
