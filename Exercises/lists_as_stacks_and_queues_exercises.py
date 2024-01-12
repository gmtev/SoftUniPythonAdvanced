from collections import deque
# reverse numbers
numbers = input().split()
while numbers:
    print(numbers.pop(), end=" ")

# other solution
numbers = deque(input().split())
for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")

# numbers = deque(input() .split())
# numbers.reverse()
# print(' '.join(numbers))/print(*numbers)

# stacked queries
stack = []
for _ in range(int(input())):
    numbers_given = input().split()
    command = numbers_given[0]
    if command == '1':
        stack.append(numbers_given[1])
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))
stack.reverse()
print(*stack, sep=', ')

# other solution
stack = []
map_functions = {
    '1': lambda x: stack.append(x[1]),
    '2': lambda x: stack.pop() if stack else None,  # x isn't mandatory here
    '3': lambda x: print(max(stack)) if stack else None,
    '4': lambda x: print(min(stack)) if stack else None
}
for _ in range(int(input())):
    numbers_given = input().split()
    command = numbers_given[0]
    map_functions[command](numbers_given)
stack.reverse()
print(*stack, sep=', ')

# fast food
food_available = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))
while orders:
    current_order = orders.popleft()
    if food_available >= current_order:
        food_available -= current_order
    else:
        print(f"Orders left:", current_order, *orders)
        break
else:
    print("Orders complete")
# or with a "for" cycle
for order in orders.copy():
    if food_available >= order:
        orders.popleft()
        food_available -= order
    else:
        print(f"Orders left:", *orders)
        break
else:
    print("Orders complete")

# fashion boutique
clothes = [int(i) for i in input().split()]
capacity = int(input())
current_capacity = capacity
racks = 1
while clothes:
    current = clothes.pop()
    if current < current_capacity:
        current_capacity -= current
    elif current == current_capacity:
        if clothes:
            racks += 1
            current_capacity = capacity
    elif current > current_capacity:
        racks += 1
        current_capacity = capacity
        current_capacity -= current
#   else:
#       racks += 1
#       current_capacity = capacity - current
print(racks)

# truck tour
pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])  # return a list of numbers on each iteration
# for _ in range(int(input)):
#   pumps_data.append([int(x) for x in input().split()]
pumps_data_copy = pumps_data.copy()
gas_in_tank = 0
index = 0
while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas_in_tank += petrol
    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_in_tank = 0
print(index)


# balanced parentheses
sequence = deque(input())
opening_brackets = "([{"
closing_brackets = ")]}"
counter = 0

while sequence and counter < len(sequence) / 2:
    if sequence[0] not in opening_brackets:
        break
    index = opening_brackets.index(sequence[0])
    if sequence[1] == closing_brackets[index]:
        sequence.popleft()
        sequence.popleft()
        sequence.rotate(counter)
        counter = 0
    else:
        sequence.rotate(-1)
        counter += 1
if sequence:
    print("NO")
else:
    print("YES")

# robotics
