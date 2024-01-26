# negatives vs. positives
def print_numbers(nums):
    positive = sum(num for num in nums if num > 0)
    negative = sum(num for num in nums if num < 0)

    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
print_numbers(numbers)

# keyword argument length


def kwargs_length(**kwargs) -> int:
    return len(kwargs)


# even or odd
def even_odd(*args):
    command = args[-1]
    if command == 'even':
        return [num for num in args[:-1] if num % 2 == 0]
    else:
        return [num for num in args[:-1] if num % 2 != 0]


# numbers filter
def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs['odd'] = [num for num in kwargs['odd'] if num % 2 != 0]
    if "even" in kwargs:
        kwargs['even'] = [num for num in kwargs['even'] if num % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


# concatenate
def concatenate(*args,**kwargs):
    text = ''.join(args)

    for key, value in kwargs.items():
        text = text.replace(key, value)
    return text


# function executor
def func_executor(*args):
    result = []
    for function, arguments in args:
        result.append(f'{function.__name__} - {function(*arguments)}')

    return '\n'.join(result)
    # return '\n'.join(f'{function.__name__} - {function(*arguments)}'for function, arguments in args)


# grocery
def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for product, quantity in products:
        result.append(f'{product}: {quantity}')

    return '\n'.join(result)


# age assignment
def age_assignment(*args, **kwargs):
    result = []
    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return '\n'.join(sorted(result))


# recursion palindrome
def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[-index-1]:
        return f"{word} is not a palindrome"

    return palindrome(word, index+1)

# fill the box
from collections import deque


def fill_the_box(h,l,w, *args):
    space = h * l * w
    cubes = deque(args)
    while cubes[0] != "Finish":
        space -= cubes.popleft()
        if space < 0:
            cubes_left = sum (c for c in cubes if c != "Finish")
            return f"No more free space! You have {cubes_left + abs(space)} more cubes."
    return f"There is free space in the box. You could put {space} more cubes."


# math operations
def math_operations(*args, **kwargs):
    keys = list(kwargs.keys())
    for i in range(len(args)):
        key = keys[i % 4]
        if key == "a":
            kwargs[key] += args[i]
        elif key == "s":
            kwargs[key] -= args[i]
        elif key == "d":
            if args[i] != 0:
                kwargs[key] /= args[i]
        elif key == "m":
            kwargs[key] *= args[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f"{k}: {v:.1f}" for k, v in kwargs)
