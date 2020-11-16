# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange, sample
import sys
from os import path


try:
    for_seed, upper_bound, size =\
         (int(x) for x in input('Enter three nonnegative integers: ').split())
    if for_seed < 0 or upper_bound < 0 or size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
w = len(str(upper_bound - 1))
with open('mapping.txt', 'w') as mapping:
    for (a, b) in zip(sorted(randrange(upper_bound) for _ in range(size)),
                      (randrange(upper_bound) for _ in range(size))
                     ):
        print(f'{a:{w}}', '->', b, file=mapping)
print('Here is the mapping that has been generated:')
with open('mapping.txt') as mapping:
    for line in mapping:
        print(line, end='')

valid_mapping = True
most_frequent_inputs = []
function = {}

# INSERT YOUR CODE HERE
from collections import defaultdict
data_mapping = defaultdict(list)
list1 = []
list2 = []
with open('mapping.txt') as mapping:
    for line in mapping:
        line_value = line.split('->')
        left_column = int(line_value[0].strip())
        right_column = int(line_value[1].strip())
        list1.append(left_column)
        list2.append(right_column)

        if right_column in data_mapping[left_column]:
            valid_mapping = False
        data_mapping[left_column].append(right_column)

i = 0
max_length = 0
while i < len(list1):
    count_number = list1.count(list1[i])
    max_length = max(max_length, count_number)
    i +=1

for x in list1:
    if max_length == list1.count(x) and x not in most_frequent_inputs:
        most_frequent_inputs.append(x)

for i in range(len(list1)):
    x = list1[i]
    count_number = list1.count(x)
    if count_number == 1:
        function[list1[i]] = list2[i]





if not valid_mapping:
    print("Sorry, that's not a correct mapping.")
else:
    print("Ok, that's a correct mapping.")
    print('The list of most frequent inputs is:\n\t', most_frequent_inputs)
    print('The function extracted from the mapping is:\n\t', function)