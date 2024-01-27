# so many exceptions
# this one is just manual editing of the code
numbers_list = [int(x) for x in (input().split(", "))]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)

# repeat text
text = input()
try:
    times = int(input())
    print(text*times)
except ValueError:
    print('Variable "times" must be an integer')

# value cannot be negative
class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative("Value cannot be negative!")
