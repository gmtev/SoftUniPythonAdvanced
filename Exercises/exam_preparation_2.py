# monster extermination
from collections import deque

monsters = deque([int(el) for el in input().split(',')])
attacks = [int(el) for el in input().split(',')]
kills = 0

while monsters and attacks:
    monster = monsters.popleft()
    attack = attacks.pop()
    if attack >= monster:
        kills += 1
        attack -= monster
        if attacks:
            attacks[-1] += attack
        elif not attacks and attack > 0:
            attacks.append(attack)
    else:
        monster -= attack
        monsters.append(monster)

if not monsters:
    print("All monsters have been killed!")
if not attacks:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {kills}")

# delivery boy

r, c = [int(x) for x in input().split()]
matrix = []
boy_coordinates = []

directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)
}
for _ in range(r):
    line = list(input())
    matrix.append(line)

command = ' '

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "B":
            boy_coordinates = [i, j]
            boy_starting = boy_coordinates

while command:
    command = input()
    row, col = boy_coordinates
    row += directions[command][0]
    col += directions[command][1]
    if 0 <= row < r and 0 <= col < c:
        if matrix[row][col] == "P":
            matrix[boy_coordinates[0]][boy_coordinates[1]] = '.'
            boy_coordinates = [row, col]
            matrix[row][col] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
            continue

        if matrix[row][col] == "*":
            continue

        if matrix[row][col] == "A":
            matrix[boy_coordinates[0]][boy_coordinates[1]] = '.'
            boy_coordinates = [row, col]
            matrix[row][col] = 'P'
            print("Pizza is delivered on time! Next order...")
            matrix[boy_starting[0]][boy_starting[1]] = "B"
            break

        if not matrix[boy_coordinates[0]][boy_coordinates[1]] == 'R':
            matrix[boy_coordinates[0]][boy_coordinates[1]] = '.'

        boy_coordinates = [row, col]
        matrix[row][col] = '.'

    else:
        matrix[boy_starting[0]][boy_starting[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

for row in matrix:
    print(*row, sep='')

# pets hotel


def accommodate_new_pets(capacity, limit, *args):
    pets = {}
    result = ''

    for pet, weight in args:
        if capacity == 0:
            result = "You did not manage to accommodate all pets!\n"
            break
        if weight <= limit:
            if pet not in pets:
                pets[pet] = 0
            pets[pet] += 1
            capacity -= 1
        else:
            continue

    else:
        result = f"All pets are accommodated! Available capacity: {capacity}.\n"
    sorted_pets = dict(sorted(pets.items()))

    result += 'Accommodated pets:\n'
    for pet, amount in sorted_pets.items():
        result += f"{pet}: {amount}\n"
    return result
