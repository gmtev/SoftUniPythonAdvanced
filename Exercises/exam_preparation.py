from collections import deque
# off-road challenge
fuel = [int(el) for el in input().split()]
altitudes = deque([int(el) for el in input().split()])
fuel_needed = deque([int(el) for el in input().split()])
counter = 0
top_reached = True
reached = []

while fuel:
    current_fuel = fuel.pop() - altitudes.popleft()
    counter += 1
    if current_fuel >= fuel_needed.popleft():
        print(f"John has reached: Altitude {counter}")
        reached.append(f"Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter}")
        counter -= 1
        top_reached = False
        break

if top_reached:
    print(f"John has reached all the altitudes and managed to reach the top!")

else:
    print("John failed to reach the top.")
    if reached:
        print(f"Reached altitudes: {', '.join(reached)}")
    else:
        print("John didn't reach any altitude.")

# fishing competition
size = int(input())
matrix = []
ship_coordinates = []
whirlpool = False
quota = 0
directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)

}
for row in range(size):
    info = list(input())
    matrix.append(info)

for row in range(size):
    for column in range(size):
        if matrix[row][column] == "S":
            ship_coordinates = [row, column]

while True:
    command = input()
    if command == "collect the nets":
        break
    r, c = ship_coordinates
    matrix[r][c] = "-"
    row = r + directions[command][0]
    col = c + directions[command][1]

    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    if col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    ship_coordinates = [row, col]
    if matrix[row][col].isdigit():
        quota += int(matrix[row][col])
    elif matrix[row][col] == "W":
        whirlpool = True
        break
    matrix[row][col] = "S"


if whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{ship_coordinates[0]},{ship_coordinates[1]}]")
else:
    if quota >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - quota} tons of fish more.")
    if quota > 0:
        print(f"Amount of fish caught: {quota} tons.")
    for row in matrix:
        print(*row, sep="")

# team line-up


def team_lineup(*args):
    teams = {}
    for player, country in args:
        if country not in teams:
            teams[country] = []

        teams[country].append(player)
    sorted_teams = dict(sorted(teams.items(), key=lambda x: (-len(x[1]), (x[0]))))

    result = ''
    for country, player_names in sorted_teams.items():
        result += f'{country}:\n'

        for player in player_names:
            result += f"  -{player}\n"
    return result
