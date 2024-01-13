# count same values
numbers = tuple([float(number) for number in input().split()])
numbers_and_occurrences = {}
for num in numbers:
    if num not in numbers_and_occurrences:
        numbers_and_occurrences[num] = numbers.count(num)

for number, occurrence in numbers_and_occurrences.items():
    print(f"{number} - {occurrence} times")

# students grades
students = int(input())
students_grades = {}
for _ in range(students):
    name, grade_string = input().split()
    grade = float(grade_string)
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for name, grades in students_grades.items():
    avg_grade = sum(grades)/len(grades)
    formatted_grades = f"{' '.join([f'{grade:.2f}' for grade in grades])}"
    print(f'{name} -> {formatted_grades} (avg: {avg_grade:.2f})')

# record unique names
number_of_names = int(input())
unique_names = set()
for _ in range(number_of_names):
    unique_names.add(input())
for name in unique_names:
    print(name)

# parking lot
amount_of_cars = int(input())
cars = set()
for _ in range(amount_of_cars):
    direction, car_number = input().split(', ')
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        if car_number in cars:
            cars.remove(car_number)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")

# SoftUni party
number_of_guests = int(input())
passes = set()
for _ in range(number_of_guests):
    passes.add(input())
guest_pass = input()
while guest_pass != "END":
    if guest_pass in passes:
        passes.remove(guest_pass)
    guest_pass = input()
print(len(passes))
for guest_pass in sorted(passes):
    print(guest_pass)

