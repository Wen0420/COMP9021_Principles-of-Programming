# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange, sample
import sys
from os import path

potential_symbols = list('~!@#$%^&*+')
try:
    for_seed, nb_of_symbols = (int(x) for x in input(
        'Enter two integers, the second one being between 1 and 10 included: '
    ).split()
                               )
    if not 1 < nb_of_symbols < 11:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
# THE LIST OF SYMBOLS YOU WILL WORK WITH
symbols = list(sample(potential_symbols, nb_of_symbols))
# THE LIST OF NUMBERS YOU WILL WORK WITH
repetitions = list(randrange(1, 10) for _ in range(nb_of_symbols))
print('Here is the list of symbols:')
print('    ', symbols)
print('Here is the list of how many times each of them is to be displayed:')
print('    ', repetitions)
# THE SYMBOL YOU WILL WORK WITH
chosen_symbol = input('What is your favourite symbol? ')
try:
    # THE NUMBER YOU WILL WORK WITH
    gap = int(input('How big do you want the gap to be '
                    '(should be 1 or more)? '
                    )
              )
    if gap < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if chosen_symbol not in symbols:
    print("Sorry, I don't recognise that symbol.")
    sys.exit()
# THE NAME OF THE FILE YOU WILL WORK WITH
instructions_file_name = input('What is the name of the file containing '
                               'the instructions? '
                               )
if not path.exists(instructions_file_name):
    print('Sorry, there is no such file.')
    sys.exit()

# INSERT YOUR CODE BELOW


print("I have a drawing for you...")
index = symbols.index(chosen_symbol)
result = {}
for i in range(len(symbols)):
    result[symbols[i]] = repetitions[i]
    if symbols[i] == chosen_symbol:
        index = i
    break

repetitions_number = repetitions[index]

print(f"It is made of {chosen_symbol}, repeated ", end='')
if repetitions_number == 1:
    print("once,")
else:
    print(f"{repetitions_number} times,")

print(f"placed in the four corners of a rectangle,\nwith a gap of {gap} both horizontally and vertically.\n")

print(chosen_symbol * int(repetitions_number) + ' ' * gap + chosen_symbol * int(repetitions_number))

print('\n' * (gap - 1))

print(chosen_symbol * int(repetitions_number) + ' ' * gap + chosen_symbol * int(repetitions_number) + '\n')

print("Like it?")

print("I am now going to process the instructions in the file.\n")

with open(instructions_file_name) as file:
    lines = []
    for line in file:
        if line.startswith("Draw a line of "):
            values = line.split()
            symbol_number = values[4]
            symbol = values[5]
            space_number = values[7]
            print(int(space_number) * ' ' + int(symbol_number) * symbol)

print("\n".join(lines))

print("Ok, but not a great drawing...")
