# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Generates a list L of random positive integers, at least one
# of which is strictly positive, and prints out:
# - a list "fractions" of strings of the form 'a/b' such that:
#   . a <= b,
#   . a*n and b*n both occur in L for some n, and
#   . a/b is in reduced form
# enumerated from smallest fraction to largest fraction
#  (0 and 1 are exceptions, being represented as such rather than as
# 0/1 and 1/1);
# - if "fractions" contains 1/2, then the fact that 1/2 belongs to "fractions";
# - otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
#  if that member is unique;
# - otherwise, the two members "closest_1" and "closest_2" of "fractions" that
# are closest to 1/2, in their natural order.


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = (int(x) for x in
                      input('Enter three nonnegative integers: ').split()
                                      )
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# INSERT YOUR CODE HERE

from fractions import Fraction

from fractions import Fraction
sorted_List = list(sorted(L))
compute_fraction = {}
from collections import defaultdict
closest = defaultdict(list)

for a in range(len(sorted_List)):
    numerator = sorted_List[a]
    for b in range(len(sorted_List)):
        denominator = sorted_List[b]
        if numerator <= denominator and denominator != 0:
            key = Fraction(numerator, denominator)
            str_key = str(key)
            compute_fraction[key] = str_key
            fractions.append(key)

for key, str_key in list(compute_fraction.items()):
    if abs(key - 0.5) not in closest:
        compute_fraction[abs(key - 0.5)] = []
        compute_fraction[abs(key - 0.5)].append(str_key)
    else:
        pass
    closest[abs(key - 0.5)].append(key)

values = list(compute_fraction.values())


for x in fractions:
    if x == Fraction(1, 2):
        spot_on = True
    else:
        if len(closest[min(closest.keys())]) == 1:
            closest_1 = closest[min(closest.keys())][0]
        else:
            closest_1, closest_2 = sorted(closest[min(closest.keys())])

fractions = []
for x in sorted(set(fractions)):
    fractions.append(str(x))









print('\nThe fractions no greater than 1 that can be built from L, '
      'from smallest to largest, are:'
     )
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')