# diagonals
rows_and_columns = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows_and_columns)]

primary = [matrix[x][x] for x in range(rows_and_columns)]
secondary = [matrix[x][rows_and_columns - x - 1] for x in range(rows_and_columns)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")

# diagonal difference
rows_and_columns = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_and_columns)]
primary_sum = 0
secondary_sum = 0

for i in range(rows_and_columns):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][rows_and_columns - i - 1]

print(abs(primary_sum - secondary_sum))

# 2x2 squares in a matrix
rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
equal_squares = 0

for row in range(rows-1):
    for col in range(columns-1):
        element = matrix[row][col]
        if element == matrix[row][col+1] and element == matrix[row+1][col] and element == matrix[row+1][col+1]:
            equal_squares += 1

print(equal_squares)

# maximal sum
rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
maximal_sum = float('-inf')
biggest_matrix = []
for row in range(rows-2):
    for col in range(columns-2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row+1][col:col + 3]
        third_row = matrix[row+2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > maximal_sum:
            maximal_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]
print(f"Sum = {maximal_sum}")
[print(*row) for row in biggest_matrix]

# matrix of palindromes
rows, columns = [int(x) for x in input().split()]
start = ord('a')
for row in range(start, start+rows):
    for column in range(row, row + columns):
        print(chr(row), chr(column), chr(row), sep='', end=' ')
    print()


# matrix shuffling
def check_indices_valid(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_elements(command, indices):
    if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
valid_rows = range(rows)
valid_cols = range(columns)

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]
    if command_type == "END":
        break

    swap_elements(command_type, coordinates)

# snake moves
from collections import deque

rows, columns = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < columns:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(columns)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(columns)][::-1], sep="")
