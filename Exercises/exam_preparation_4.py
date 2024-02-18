# temple of doom
from collections import deque
tools = deque([int(el) for el in input().split()])
substances = [int(el) for el in input().split()]
challenges = [int(el) for el in input().split()]

while challenges and substances:
    current_tool = tools.popleft()
    current_substance = substances[-1]
    result = current_tool * current_substance
    if result in challenges:
        challenges.remove(result)
        substances.pop()
        continue
    else:
        current_tool += 1
        tools.append(current_tool)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()
if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if substances:
    print(f"Substances: {', '.join(str(el) for el in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(el) for el in challenges)}")


# mouse in the kitchen
def cheese_checker(field):
    for row in field:
        for el in row:
            if el == "C":
                return True
    return False


n,m = (int(el) for el in input().split(','))
matrix = []
coordinates = []

directions = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)

}
for roww in range(n):
    line = list(input())
    if "M" in line:
        coordinates = [roww, line.index("M")]
    matrix.append(line)


while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break
    r, c = coordinates
    next_r = r + directions[command][0]
    next_c = c + directions[command][1]
    if not (0 <= next_r < n and 0 <= next_c < m):
        print("No more cheese for tonight!")
        break
    else:
        if matrix[next_r][next_c] == "C":
            matrix[r][c] = "*"
            matrix[next_r][next_c] = "M"
            coordinates = [next_r, next_c]
            if not cheese_checker(matrix):
                print("Happy mouse! All the cheese is eaten, good night!")
                break
            continue
        elif matrix[next_r][next_c] == "@":
            continue
        elif matrix[next_r][next_c] == "T":
            matrix[r][c] = "*"
            matrix[next_r][next_c] = "M"
            print("Mouse is trapped!")
            break
        matrix[r][c] = "*"
        matrix[next_r][next_c] = "M"
        coordinates = [next_r,next_c]

for row in matrix:
    print(*row, sep="")

# enrollment
def gather_credits(credits_needed, *args):
    result = []
    current_credits = 0
    for course, credits in args:
        if current_credits >= credits_needed:
            break
        if course in result:
            continue
        if current_credits < credits_needed:
            result.append(course)
            current_credits += int(credits)

    if current_credits >= credits_needed:
        return f"Enrollment finished! Maximum credits: {current_credits}.\n" \
               f"Courses: {', '.join(sorted(result))}"
    return f"You need to enroll in more courses! You have to gather {credits_needed - current_credits} credits more."