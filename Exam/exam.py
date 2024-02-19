# chicken snack
from collections import deque
money = deque([int(el) for el in input().split()])
price = deque([int(el) for el in input().split()])
food = 0
while money and price:
    current_money = money[-1]
    current_price = price[0]
    if current_price == current_money:
        food += 1
        money.pop()
        price.popleft()
    elif current_money > current_price:
        food += 1
        current_money -= current_price
        money.pop()
        price.popleft()
        if money:
            money[-1] += current_money
    else:
        money.pop()
        price.popleft()

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")
elif food == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food == 1:
    print(f"Henry ate: {food} food.")
else:
    print(f"Henry ate: {food} foods.")

# clear skies
def enemy_checker(matrix):
    for row in matrix:
        for el in row:
            if el == "E":
                return True
    return False

size = int(input())
matrix = []
position = []

armor = 300
directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)

}

for row in range(size):
    line = list(input())
    if "J" in line:
        position = [row, line.index("J")]
    matrix.append(line)


command = input()
while True:
    r, c = position
    next_r = r + directions[command][0]
    next_c = c + directions[command][1]
    matrix[r][c] = "-"
    if matrix[next_r][next_c] == "E":
        matrix[next_r][next_c] = "J"
        if not enemy_checker(matrix):
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        armor -= 100
        if armor <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_r}, {next_c}]!")
            break
    elif matrix[next_r][next_c] == "R":
        if armor < 300:
            armor = 300
    matrix[next_r][next_c] = "J"
    position = [next_r, next_c]
    command = input()

for row in matrix:
    print(*row, sep='')

# cookbook
def cookbook(*args):
    result = ""
    recipes = {}
    for name, cuisine, ingredients in args:
        if cuisine not in recipes:
            recipes[cuisine] = []
        recipes[cuisine].append((name, ingredients))
    sorted_cuisines = dict(sorted(recipes.items(), key=lambda x: (-len(x[1]), (x[0]))))
    for cuisine in sorted_cuisines:
            result += f"{cuisine} cuisine contains {len(recipes[cuisine])} recipes:\n"
            sorted_recipes = sorted(recipes[cuisine], key=lambda x: x[0])
            for recipe in sorted_recipes:
                result += f"  * {recipe[0]} -> Ingredients: {', '.join(recipe[1])}\n"
    return result