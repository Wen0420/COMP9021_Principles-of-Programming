import sys

import sys
from copy import deepcopy
#input1 Please input the heroes' powers:
try:
    power = input('Please input the heroes\' powers: ').split()
    power = [int(x) for x in power]
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
#input2 Please input the number of power flips:
try:
    nb_of_switches = int(input('Please input the number of power flips: '))
    if int(nb_of_switches) < 0 or int(nb_of_switches) > len(power):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
#多次发现同一个英雄的力量, 将最小的数字从列表中找出， then sum
#n = times
def same_power(L, param_nb_of_switches):
    # 对列表进行排序
    # 每一次找到最小，并sort，再找最小
    L1 = [x for x in sorted(L)]
    for n in range(0, param_nb_of_switches):
        L1[0] = 0 - L1[0]
        L1.sort()

    return sum(L1)

#最多一次发现同一个英雄的力量，将L1中最小的数,取出放在L2， then sum L2
def max_1power(L, param_nb_of_switches):
    L1 = [x for x in sorted(L)]
    for index in range(0, param_nb_of_switches):
        L1[index] = 0 - L1[index]
    return sum(L1)

#翻转许多连续的英雄，最大的可实现的力量
def max_power_csHero(L, param_nb_of_switches):

    # L = 1 2 3 4       10
    # L = -1 -2 -3  4   -2
    # param_nb_of_switches = 3

    total = sum(L)
    sumL3 = []
    for index in range(0, len(L) - param_nb_of_switches + 1):
        flipping_sum = sum(L[index: index + param_nb_of_switches])
        current_total = total - 2 * flipping_sum
        sumL3.append(current_total)

    return max(sumL3)

#任意翻转许多连续的英雄的力量，最大可达到的力量
def max_power_arcsHero(L):
    sumL4 = []
    # sumL4.append(count)
    # for i in range(0, len(L)):
    #     number = count
    #     if L[i] < 0:
    #         for times in range(i, len(L)):
    #             number = number + (-1 * 2 * L[times])
    #             if number > sumL4[0]:
    #                 sumL4.append(number)
    #             else:
    #                 break

    # greedy search
    # 取子序列的最大值，跟count相加
    temp = 0
    for item in L:
        temp += 0 - item
        if temp > 0:
            sumL4.append(temp)
        else:
            temp = 0
    if sumL4:
        return count + 2 * max(sumL4)
    else:
        return count

count = sum(power)
q1 = same_power(power, nb_of_switches)
q2 = max_1power(power, nb_of_switches)
q3 = max_power_csHero(power, nb_of_switches)
q4 = max_power_arcsHero(power)

print('Possibly flipping the power of the same hero many times, the greatest achievable power is {}.\n'
'Flipping the power of the same hero at most once, the greatest achievable power is {}.\n'
'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {}.\n'
'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {}.'.format(q1, q2, q3, q4))









