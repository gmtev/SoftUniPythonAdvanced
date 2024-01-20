# sum_matrix_elements
rows, columns = [int(x) for x in input().split(', ')]
matrix = []
total = 0

for i in range(rows):
    elements = [int(x) for x in input().split(', ')]
    total += sum(elements)
    matrix.append(elements)

print(total)
print(matrix)

# even matrix
rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(i) for i in input().split(', ') if int(i) % 2 == 0])

print(matrix)

# flattening matrix
rows = int(input())
matrix = []
flattened = []

for _ in range(rows):
    matrix.append([int(i) for i in input().split(', ')])
    flattened = [element for row in matrix for element in row]

print(flattened)

# second solution
rows = int(input())
flattened = []

for _ in range(rows):
    row = [int(i) for i in input().split(', ')]
    flattened.extend(row)

print(flattened)

# sum matrix columns
rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for column_index in range(columns):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][column_index]
    print(col_sum)

# primary diagonal
rows_and_columns = int(input())
matrix = []
diagonal_sum = 0

for _ in range(rows_and_columns):
    matrix.append([int(x) for x in input().split()])

for row_index in range(rows_and_columns):
    for column_index in range(rows_and_columns):
        if column_index == row_index:
            diagonal_sum += matrix[column_index][row_index]

print(diagonal_sum)
# for row_and_column_index in range(rows_and_columns):
#   diagonal_sum += matrix[row_and_column_index][row_and_column_index]

# symbol in matrix
rows_and_columns = int(input())
matrix = []
symbol_found = False

for _ in range(rows_and_columns):
    matrix.append([x for x in input()])

symbol_needed = input()
for row_index in range(rows_and_columns):
    if symbol_found:
        break
    for column_index in range(len(matrix[row_index])):
        if matrix[row_index][column_index] == symbol_needed:
            print(f'({row_index}, {column_index})')
            symbol_found = True
            break

if not symbol_found:
    print(f"{symbol_needed} does not occur in the matrix")

# square with maximum sum
rows, columns = [int(x) for x in input().split(', ')]
matrix = []
current_max_sum = 0
largest_square = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row_index in range(rows-1):
    for column_index in range(columns-1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index+1]
        lower_element = matrix[row_index+1][column_index]
        diagonal_element = matrix[row_index+1][column_index+1]
        total_sum = current_element + next_element + lower_element + diagonal_element

        if total_sum > current_max_sum:
            current_max_sum = total_sum
            largest_square = [[current_element, next_element], [lower_element, diagonal_element]]

print(*largest_square[0])
print(*largest_square[1])
print(current_max_sum)