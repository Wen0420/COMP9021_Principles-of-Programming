#input() 函数,内置函数
#nput() 函数接受一个标准输入数据，返回为 string 类型。
#语法：input([prompt])
#prompt: 提示信息
L = input('Enter your name:')
print('Hello, ' + L)

x = input('How many times do you want to play? ')#输入10_000
print(x)#10_000
x = int(x)
print(x)#10000

#上面的可以直接变为
x = int(input('How many times do you want to play? '))#输入10_000
print(x)#10000

try:
    x = int(input('How many times do you want to play? '))
except ValueError:
    print('Bad input, try again')#when bad input happend we should do the whole try again, for doing this we should use while

while True:
    try:
        x = int(input('How many times do you want to play? '))
        break#means if this is true then we get out of this loop
    except ValueError:
        print('Bad input, try again')

while True:
    try:
        nb_of_times =\
            int(input('How many times do you want to play? '))
        break
    except ValueError:
        print('Bad input, try again')
print('I keep in mind you want to play', nb_of_times, 'times')

#in case the input is negative, we want to solve this problem,#back slash means the statement continues in the next line.
while True:
    try:
        nb_of_times =\
            int(input('How many times do you want to play? '))
        if nb_of_times < 1:
            raise ValueError
        break
    except ValueError:
        print('Bad input, try again')
print('I keep in mind you want to play', nb_of_times, 'times')

#The dir() method tries to return a list of valid attributes of the object.
dir(str)
help(str.isalpha)# help tell me about this isalpha gonna to apply to strings

#istittle means: test for is this caiptalised
'Hello'.istitle()
#the result is: True
'HELLO'.lower()

contestant_switches = input('Do you want the contestant to switch?')
if contestant_switches.istitle():
    contestant_switches = contestant_switches.lower()
print(contestant_switches)

contestant_switches = input('Do you want the contestant to switch?')
if contestant_switches.istitle():
    contestant_switches = contestant_switches.lower()
if contestant_switches in ('yes', 'y'):
    contestant_switches = True
if contestant_switches in ('no', 'n'):
    contestant_switches = False
print(contestant_switches)


while True:
    contestant_switches = input('Do you want the contestant to switch?')
    if contestant_switches.istitle():
        contestant_switches = contestant_switches.lower()
    if contestant_switches in ('yes', 'y'):
        contestant_switches = True
        break
    if contestant_switches in ('no', 'n'):
        contestant_switches = False
        break
    print('Bad input, try again')
print(contestant_switches)

doors = ['A', 'B', 'C']
print(doors)
doors = list('ABC')
print(doors)

#{} is for set, [] for list, the difference bewteen set and list is set can be sorted
L = [1, 3, 4]
S = {1, 2, 4}
print(L[0])# I can ask the first element of list
print(S[0])# we cannot ask the first element of list this will causes TypeError

print(type({2})) #set
print(type({2: 20})) #dict
print(type({})) #dict
print(set()) #set
print(dict()) #dict

print(doors)
import random
dir(random)

random.choice(doors)
#other way
from random import choice
print(choice(doors))

from random import *
print(choice[1, 2, 3])#it will show all the founctions related to random

#choice is use for index, tuple or list but cannot use for a set
doors = ['A', 'B', 'C']# winning doors is one of the A B C, same as my first choice
winning_doors = choice(doors)
print(winning_doors)

first_choice = choice(doors)
doors.remove(first_choice)
print(first_choice)

print(doors)
#the result is first line:'A', second line:'B', third line ['A', 'C'] means the winning door is A, the contestant decide to choose
# B,and then we remove B from the list

print(randrange(5))# this will randomly give a result bewteen 0 to 5 -1

#pop out the last element of the list
L = list('asdfghj')
print(L)
L.pop()
print(L)
L.pop()
print(L)
# the other is to private the particular location, it is pop out the string in that particular location
L = list('asdfghj')
print(L)
L.pop(3)
print(L)
L.pop(3)
print(L)

doors = ['A', 'B', 'C']# winning doors is one of the A B C, same as my first choice
winning_doors = choice(doors)
print(winning_doors)

#first_choice = choice(doors)
#doors.remove(first_choice)
first_choice = doors.pop(randrange(3))#give me a random index 0 1 or 2, and then pop out this number
print(first_choice)

print(doors)

#give me a random index 0 1 or 2

doors = ['A', 'B', 'C']
# 3 possible outcomes
winning_door = choice(doors)
# 3 possible outomes
first_chosen_door = doors.pop(randrange(3))
if first_chosen_door == winning_door:
# 2 possible outcomes
    opened_door = doors.pop(randrange(2))
else:
    doors.remove(winning_door)
    opened_door = doors[0]
print(winning_door)
# Possibly identical to previous
print(first_chosen_door)
# Necessarily different to previous two
print(opened_door)


while True:
    contestant_switches = input('Should the contestant switch? ')
    if contestant_switches.istitle():
        contestant_switches = contestant_switches.lower()
    if contestant_switches in {'yes', 'y'}:
        contestant_switches = True
        print('I keep in mind you want to switch.')
        break
    if contestant_switches.lower() in {'no', 'n'}:
        contestant_switches = False
        print("I keep in mind you don't want to switch.")
        break
    print('Your input is incorrect, try again.')
doors = ['A', 'B', 'C']
# 3 possible outcomes
winning_door = choice(doors)
# 3 possible outomes
first_chosen_door = doors.pop(randrange(3))
if not contestant_switches:
    second_chosen_door = first_chosen_door
if first_chosen_door == winning_door:
# 2 possible outcomes
    opened_door = doors.pop(randrange(2))
if contestant_switches:
    second_chosen_door = doors[0]
else:
    doors.remove(winning_door)
    opened_door = doors[0]
if contestant_switches:
    second_chosen_door = winning_door
print(winning_door)
# Possibly identical to previous
print(first_chosen_door)
# Necessarily different to previous two
print(opened_door)
# Same as first_chosen_door if contestant does not switch
# Otherwise, the unique one which is neither
# first_chosen_door nor opened_door
print(second_chosen_door)

# for loop
for i in range(4):
    print(i, i * 2)

E = iter(range(4)) #interator
print(E)
print(next(E))
print(next(E))
print(next(E))

def f(x, y, u=10, v=20):#10 and 20 are default values
    print(x, y, u, v)
f(1, 2, 3, 4)
f(1, 2, 3)
f(1, 2)

