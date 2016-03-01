__author__ = 'wolfram'

import sys

def squares(a):
    if len(a) < 3:
        return 0
    square = 0
    while len(a) >= 3:
        left = find_left(a)
        check_on_reverse = False
        count = 0
        for i in range(left + 1, len(a)):
            if (a[i - 1] - a[i] < 0) & (check_on_reverse == False):
                check_on_reverse = True
            if a[left] - a[i] > 0:
                count += a[left] - a[i]
            else:
                a = a[i:]
                break
        if i == len(a) - 1:
            if check_on_reverse == True:
                a = [j for j in reversed(a)]
            else:
                return square
        if (i != len(a) - 1) & (count > square):
            square = count
    return square


def find_left(a):
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            return i - 1
    return 0

if __name__ == "__main__":
    a = sys.stdin.readline().split()
    a = [int(i) for i in a]
    sys.stdout.write(str(squares(a)))