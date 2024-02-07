# for the triangle
def print_triangle(n):
    print_upper_half(n)
    print_lower_half(n)


def print_upper_half(n):
    for row in range(1, n+1):
        for num in range(1, row+1):
            print(num, end=' ')
        print()


def print_lower_half(n):
    for row in range(n, 0, -1):
        for num in range(1, row):
            print(num, end=' ')
        print()


# for the mathematical operations
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


def power(num_1, num_2):
    return num_1 ** num_2


sign_mapper = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power
}


def execute_expression(expression):
    num_1_str, sign, num_2_str = expression.split()
    num_1 = float(num_1_str)
    num_2 = int(num_2_str)
    return sign_mapper[sign](num_1, num_2)


# for the fibonacci sequence
def create_sequence(number):
    seq = [0, 1]

    for _ in range(number-2):
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)

    return seq


def locate_number(number, sequence):
    try:
        return f"The number {number} is at index {sequence.index(number)}."

    except ValueError:
        return f"The number {number} is not in the sequence!"
