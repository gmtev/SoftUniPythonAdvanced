from collections import deque
# reverse numbers
numbers = input().split()
while numbers:
    print(numbers.pop(), end=" ")

# stacked queries
stack = []
final = []
N = int(input())
for i in range(N):
    command = input().split()
    if len(command) > 1:
        stack.append(int(command[1]))
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        stack_num = [int(i) for i in stack]
        print(max(stack_num))
    elif command[0] == "4":
        stack_num = [int(i) for i in stack]
        print(min(stack_num))
while stack:
    final.append(str(stack.pop()))
print(', '.join(final))

# fast food
food_available = int(input())
orders = deque(input().split())
orders_int = [int(i) for i in orders]
print(max(orders_int))
while orders:
    current_order = int(orders.popleft())
    if food_available >= current_order:
        food_available -= current_order
    else:
        orders.appendleft(str(current_order))
        break
if orders:
    print(f"Orders left: {' '.join(orders)}")
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
print(racks)

# truck tour
amount_of_pumps = int(input())
for pumps in range(amount_of_pumps):
    info = input().split()
    petrol, distance = int(info[0]), int(info[1])



# balanced parentheses
sequence = deque(input())
balanced = True
while sequence:
    left = sequence.popleft()
    right = sequence.pop()
    if left == '(' and right == ")" or left == "{" and right == "}" or left == "[" and right == "]" and len(sequence) % 2 == 0:
        continue
    else:
        balanced = False
        break
if balanced:
    print("YES")
else:
    print("NO")
