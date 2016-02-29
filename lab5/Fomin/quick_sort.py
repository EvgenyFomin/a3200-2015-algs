__author__ = 'wolfram'

import random
import sys

a = sys.stdin.readline().split()
a = [int(i) for i in a]
def sort(list):
    if len(list) <= 1:
        return list
    pivot = random.choice(list)
    less = [x for x in list if x < pivot]
    equal = [x for x in list if x == pivot]
    greater = [x for x in list if x > pivot]

    return sort(less) + equal + sort(greater)

a = sort(a)
a = [str(i) for i in a]
sys.stdout.write(' '.join(a))