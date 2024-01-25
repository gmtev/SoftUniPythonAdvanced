#
line = input().split('|')
new_matrix = []
for element in line[::-1]:
    new_matrix.extend(element.split())
print(*new_matrix)


# matrix modification
def valid_coordinates(coordinates):
    if 0 <= int(coordinates[1]) <= rows_and_columns - 1 and 0 <= int(coordinates[2]) <= rows_and_columns - 1:
        return True


rows_and_columns = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_and_columns)]
while True:
    command = list(input().split())
    if command[0] == "END":
        break
    elif command[0] == "Add" and valid_coordinates(command):
        matrix[int(command[1])][int(command[2])] += int(command[3])
    elif command[0] == "Subtract" and valid_coordinates(command):
        matrix[int(command[1])][int(command[2])] -= int(command[3])
    else:
        print("Invalid coordinates")
for row in matrix:
    print(*row)

#knight game
size = int(input())
matrix = [list(input()) for _ in range(size)]

pos_numbers = [-2, -1, 1, 2]
positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (1, 2),
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []  # [row, col]

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)

# easter bunny
rows_n_cols = int(input())
matrix = []
bunny_position = []
directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)

}
path_to_go = []
direction_to_go = ''
highest_sum = float('-inf')
for row in range(rows_n_cols):
    info = input().split()
    if "B" in info:
        bunny_position = [row,info.index("B")]
    matrix.append(info)

for direction, position in directions.items():
    r,c = [bunny_position[0]+position[0], bunny_position[1]+position[1]]
    current_sum = 0
    current_path = []
    while 0 <= r < rows_n_cols and 0 <= c < rows_n_cols:
        if matrix[r][c] == "X":
            break
        current_sum += int(matrix[r][c])
        current_path.append([r,c])
        r += position[0]
        c += position[1]
    if current_sum >= highest_sum:
        highest_sum = current_sum
        path_to_go = current_path
        direction_to_go = direction
print(direction_to_go)
for coordinates in path_to_go:
    print(coordinates)
print(highest_sum)

# alice in wonderland
size = int(input())
matrix = []
alice_position = []
tea = 0
directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)

}

for _ in range(size):
    info = input().split()
    if "A" in info:
        alice_position = [_,info.index("A")]
    matrix.append(info)
matrix[alice_position[0]][alice_position[1]] = '*'

while True:
    command = input()
    r,c = alice_position[0]+directions[command][0], alice_position[1]+directions[command][1]
    if not (0 <= r < size and 0 <= c < size):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[r][c] == "R":
        matrix[r][c] = "*"
        print("Alice didn't make it to the tea party.")
        break
    if matrix[r][c].isdigit():
        tea += int(matrix[r][c])
    matrix[r][c] = "*"
    alice_position = [r,c]
    if tea >= 10:
        print("She did it! She went to the party.")
        break
[print(*row) for row in matrix]

# range day

def move(direction: str, steps: int):
    r = my_position[0] + directions[direction][0] * steps
    c = my_position[1] + directions[direction][1] * steps
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == "x":
        return my_position
    return [r, c]


def shoot(direction: str):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]
    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
field = []
targets = 0
targets_hit = 0
targets_hit_positions = []
my_position = []  # [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    field.append(input().split())
    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]
    targets += field[row].count("x")

for _ in range(int(input())):
    command_info = input().split()  # "move up 4" -> ["move", "up", "4"]
    if command_info[0] == "move":
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_pos = shoot(command_info[1])  # [row, col] | None
        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1
        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break
if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")
print(*targets_hit_positions, sep="\n")  # [[1, 2], [3, 4]] ->