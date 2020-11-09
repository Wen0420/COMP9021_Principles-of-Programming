import os.path
import sys

from collections import defaultdict


# 笔记

import os.path
import sys


try:
    file_name = input('Please enter the name of the file you want to get data from: ')
    if not os.path.isfile(file_name):
        raise ValueError
except ValueError:
    print('Sorry, there is no such file.')
    sys.exit()

def get_longest_good_ride():
    previous_ride = 0
    good_ride_rides = []
    good_ride = 1

    for index in range(1, len(ride_list)):
        if ride_list[index] - ride_list[index - 1] == previous_ride:
            good_ride += 1
        else:
            previous_ride = ride_list[index] - ride_list[index - 1]
            good_ride = 1

        good_ride_rides.append(good_ride)

    return max(good_ride_rides)

# 简化后的：
try:
    with open(file_name) as open_file:
        ride_list = [int(item) for line in open_file if not line.isspace() for item in line.split()]
        if len(ride_list) > 1:
            first = ride_list[0]
            for second in ride_list[1:]:
                if first <= 0 or second <= 0 or first >= second:
                    raise ValueError

            q3_max_count = 0
            for i in range(len(ride_list)):
                for j in range(i + 1, len(ride_list) - q3_max_count):
                    gap = ride_list[j] - ride_list[i]
                    current_gap = 2

                    while 1:
                        if ride_list[i] + current_gap * gap in ride_list:
                            current_gap += 1
                        else:
                            break

                    q3_max_count = max(q3_max_count, current_gap)

            longest_good_ride = get_longest_good_ride()
            if longest_good_ride == len(ride_list) - 1:
                print('The ride is perfect!')
            else:
                print('The ride could be better...')
            print(f"The longest good ride has a length of: {longest_good_ride}")
            print(f"The minimal number of pillars to remove to build a perfect ride from the rest is: {len(ride_list) - q3_max_count}")
        else:
            raise ValueError

except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()


