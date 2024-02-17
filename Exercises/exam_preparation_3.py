# worms and holes
from collections import deque
worms = deque([int(el) for el in input().split()])
holes = deque([int(el) for el in input().split()])
matches = 0
all_worms = len(worms)
while worms and holes:
    current_worm = worms[-1]
    current_hole = holes[0]
    if current_worm == current_hole:
        worms.pop()
        matches += 1
    else:
        worms[-1] -= 3
    holes.popleft()
    if worms and worms[-1] <= 0:
        worms.pop()

if matches == 0:
    print("There are no matches.")
else:
    print(f"Matches: {matches}")

if not worms and matches == all_worms:
    print("Every worm found a suitable hole!")
elif not worms and matches != all_worms:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(el) for el in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(el) for el in holes)}")

# the gambler
size = int(input())
matrix = []
position = []
money = 100
lost = False
jackpot = False
directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)

}

for row in range(size):
    line = list(input())
    if "G" in line:
        position = [row, line.index("G")]
    matrix.append(line)

while money >= 0 and lost is False:
    command = input()
    if command == "end":
        break
    r, c = position
    next_r = r + directions[command][0]
    next_c = c + directions[command][1]
    if 0 <= next_r < len(matrix) and 0 <= next_c < len(matrix):
        matrix[r][c] = "-"
        symbol = matrix[next_r][next_c]
        matrix[next_r][next_c] = "G"
        if symbol == "W":
            money += 100
        elif symbol == "P":
            money -= 200
        elif symbol == "J":
            money += 100000
            jackpot = True
            break
        position = [next_r, next_c]
    else:
        lost = True

if jackpot:
    print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
elif lost or money <= 0:
    print("Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {money}$")

if money > 0:
    for row in matrix:
        print(*row, sep='')


# SoftUni Students
def softuni_students(*args, **kwargs):
    valid = {}
    invalid = []
    to_print = ""
    for id, username in args:
        if id in kwargs.keys():
            valid[username] = kwargs[id]
        else:
            invalid.append(username)

    result = dict(sorted(valid.items(), key=lambda x: x[0]))

    for student, course in result.items():
        to_print += f"*** A student with the username {student} has successfully finished the course {course}!\n"
    if invalid:
        to_print += f"!!! Invalid course students: {', '.join(sorted(invalid))}"

    return to_print
