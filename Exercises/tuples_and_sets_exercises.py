# unique usernames
number_of_names = int(input())
names = set()

for _ in range(number_of_names):
    names.add(input())

print(*names, sep='\n')
# print(*{input() for _ in range(int(input()))}, sep="\n")

# sets of elements
len_set_1, len_set_2 = [int(x) for x in input().split()]

first_set = {input() for _ in range(len_set_1)}
second_set = {input() for _ in range(len_set_2)}

print(*first_set.intersection(second_set), sep='\n')
# print(*first_set & second_set)

# periodic table
unique_elements = set()

for _ in range(int(input())):
    for element in input().split():
        unique_elements.add(element)

print(*unique_elements, sep='\n')

# count symbols
occurrences = {}

for symbol in input():
    occurrences[symbol] = occurrences.get(symbol, 0) + 1

for symbol, times in sorted(occurrences.items()):
    print(f"{symbol}: {times} time/s")

# other solution
text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")

# longest intersection
longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [element.split(',') for element in input().split('-')]
    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))
    current_intersection = first_set.intersection(second_set)  # first_set&second_set
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is "
      f"[{', '.join(str(x) for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")

# battle of names
odd_set = set()
even_set = set()

for row in range(1, int(input())+1):
    ascii_name_value = sum(ord(letter) for letter in input()) // row

    if ascii_name_value % 2 == 0:
        even_set.add(ascii_name_value)
    else:
        odd_set.add(ascii_name_value)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=', ')
elif sum_odd_set > sum_even_set:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')