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

# numbers dictionary
numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)

# email validator
from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_LENGTH = 4

pattern_valid_name = r"\w+"

email = input()

while email != "End":
    if email.count("@") > 1:
        raise MoreThanOneAtSymbol('Email should contain only one "@" symbol!')

    elif "@" not in email:
        raise MustContainAtSymbolError('Email must contain the "@" symbol!')

    elif len(email.split("@")[0]) <= MIN_NAME_LENGTH:
        raise NameTooShortError("Name is too short!")

    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}!")

    elif findall(pattern_valid_name, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    else:  # no errors raised => email is valid
        print("Email is valid")

    email = input()