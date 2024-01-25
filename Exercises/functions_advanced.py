# multiplication function
def multiply(*args):
    result = 1
    for element in args:
        result *= element
    return result


# get_info
def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


# sorting cheeses
def sorting_cheeses(**kwargs):
    result = ''
    sorted_result = sorted(kwargs.items(), key= lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese_name, quantities in sorted_result:
        result += cheese_name + '\n'
        for quantity in sorted(quantities, reverse=True):
            result += f"{quantity}\n"
    return result


# rectangle
def rectangle(length, width):
    if not isinstance(length,int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# operate
from functools import reduce


def operate(operator, *args):
    # return reduce(lambda x,y: eval(f"{x}{operator}{y}"), args)
    if operator == "+":
        return reduce(lambda x, y: x+y, args)
    elif operator == "-":
        return reduce(lambda x, y: x-y, args)
    elif operator == "*":
        return reduce(lambda x, y: x*y, args)
    elif operator == "/":
        return reduce(lambda x, y: x/y, args)


# recursive power
def recursive_power(number, power):
    # instead of return number ** power
    if power == 1:
        return number
    return number * recursive_power(number, power-1)
