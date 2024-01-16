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
