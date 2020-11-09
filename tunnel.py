

import os.path
import sys


#笔记

import os.path
import sys
import re

filename = input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(filename):
    print('Sorry, there is no such file.')
    sys.exit()

num_list = []
with open(filename) as open_file:
    for line in open_file:
        if not line.isspace():
            num_list.append(line.split())

# print(num_list)

# print(len(num_list))
if len(num_list) != 2:
    print('Sorry, input file does not store valid data.')
    sys.exit()
if len(num_list[0]) < 2 or len(num_list[1]) < 2 or len(num_list[0]) != len(num_list[1]):
    print('Sorry, input file does not store valid data.')
    sys.exit()

ceiling_list = []
floor_list = []
west_distance = 0
max_inside_tunnel = 0
try:
    for i in num_list[0]:
        ceiling_list.append(int(i))
    for j in num_list[1]:
        floor_list.append(int(j))

    max_top, min_floor = max(ceiling_list), min(floor_list)

    lines = []
    for index in range(len(floor_list)):
        top = ceiling_list[index]
        down = floor_list[index]
        if top <= down:
            raise ValueError

        line = ["0" for _ in range(min_floor, down)]
        line.extend(["1" for _ in range(down, top)])
        line.extend(["0" for _ in range(top, max_top + 1)])
        lines.append(line)




    for column_index in range(len(lines[0])):
        if lines[0][column_index] == "1":
            temp_west_distance = 1
            for row_index in range(1, len(lines)):
                if lines[row_index][column_index] == '1':
                    temp_west_distance+=1
                else:
                    break

            west_distance = max(west_distance, temp_west_distance)

    for line in zip(*lines):
        items = "".join(line).split("0")
        for item in items:
            max_inside_tunnel = max(max_inside_tunnel, len(item))

    print(f'From the west, one can into the tunnel over a distance of {west_distance}')
    print(f'Inside the tunnel, one can into the tunnel over a maximum distance of {max_inside_tunnel}')

except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()






