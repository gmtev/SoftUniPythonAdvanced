# line numbers
from string import punctuation

with open("file_2.txt", "r") as file:
    text = file.readlines()

output_file = open("created_files/output_1.txt", "w") # creating the file
for row in range(len(text)):
    letters = 0
    marks = 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {row+1}: {text[row][:-1]}  ({letters})({marks})\n")  # so that the \n isn't added


output_file.close()