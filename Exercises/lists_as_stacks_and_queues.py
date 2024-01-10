from collections import deque
# reverse strings
normal_string = list(input())
reversed_string = ''
while normal_string:
    reversed_string += normal_string.pop()
print(reversed_string)

# other way to do it
normal_string = list(input())
while normal_string:
    print(normal_string.pop(), end="")

# matching parentheses
expression = input()
parentheses_indexes = []
for index in range(0, len(expression)):
    if expression[index] == "(":
        parentheses_indexes.append(index)
    elif expression[index] == ")":
        starting_index = parentheses_indexes.pop()
        print(expression[starting_index:index+1])  # or add an "end_index" = index + 1

# supermarket
command = input()
customers = deque()
while command != "End":
    if command == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(command)
    command = input()
print(f"{len(customers)} people remaining.")

# water dispenser
water = int(input())
names = deque()
name = input()
while name != "Start":
    names.append(name)
    name = input()
command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters = int(data[0])
        person_in_line = names.popleft()
        if water >= liters:
            water -= liters
            print(f"{person_in_line} got water")
        else:
            print(f"{person_in_line} must wait")
    else:
        water += int(data[1])
    command = input()
print(f"{water} liters left")

# hot potato
names = deque(input().split())
n_toss = int(input()) - 1
while len(names) > 1:
    names.rotate(-n_toss)
    removed = names.popleft()
    print(f'Removed {removed}')
print(f"Last is {names.popleft()}")
