# calculate logarithm
from math import log
number = int(input())

try:
    base = int(input())
    print(f"{log(number, base):.2f}")

except ValueError:
    print(f"{log(number):.2f}")

# ascii art
from pyfiglet import figlet_format

text = input()

print(figlet_format(text))

# triangle
from package_for_modules.core import print_triangle

num = int(input())

print_triangle(num)

# mathematical operations
from package_for_modules.core import execute_expression

line = input()

result = execute_expression(line)
print(f"{result:.2f}")

# fibonacci sequence
from package_for_modules.core import create_sequence, locate_number

line = input()
sequence = []
while line != "Stop":
    command = line.split()
    if command[0] == "Create":
        sequence = create_sequence(int(command[2]))
        print(*sequence)

    else:
        result = locate_number(int(command[1]), sequence)
        print(result)

    line = input()
