# file opener
import os

file_name = "text.txt"
path = os.path.join("name_of_folder", file_name)

try:
    file = open(path)
    print("File found")

    file.close()

except FileNotFoundError:
    print("File is not found")

# file reader
path = os.path.join("name_of_folder", "numbers.txt")
file = open(path)

# with open(path) as file:
#   lines = file.readlines()

total_sum = 0
lines = file.readlines()
file.close()

for line in lines:
    total_sum += int(line.strip())

print(total_sum)

# file writer
with open("my_first_file.txt", "a") as file:
    file.write("I just created my first file!")

# file delete
try:
    path = os.path.join("name_of_folder", "name_of_file.txt")

    os.remove(path)

except FileNotFoundError:
    print("The file doesn't exist or is already deleted!")

# if os.path.exists()
#   os.remove(path)
# else:
#   print("The file doesn't exist or is already deleted!")

# word counter
import re
words_path = os.path.join("name_of_folder", "words.txt")
input_path = os.path.join("name_of_folder", "input.txt")
output_path = os.path.join("name_of_folder", "text.txt")
with open(words_path) as file:
    searched_words_as_text = file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()] # case-insensitive

with open(input_path) as file:
    content = file.read().lower()

words_count = {}
for searched_word in searched_words:
    regex = re.compile(rf"\b{searched_word}\b")
    result = re.findall(regex, content)  # returns a list
    words_count[searched_word] = len(result)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_path, "a") as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")
