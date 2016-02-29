__author__ = 'wolfram'

import random
import sys

def remove_equal_squares(arr):
    new_arr = []
    arr = sorted(arr)
    key = arr[0]
    new_arr.append(key)
    for i in range(1, len(arr)):
        if arr[i] != key:
            key = arr[i]
            new_arr.append(key)
    return new_arr

def squares(arr):
    arr = [pow(i, 2) for i in arr]
    arr = remove_equal_squares(arr)
    return arr

def triples(arr):
    if len(arr) < 3:
        return 0
    count = 0
    arr = squares(arr)
    for i in range(2, len(arr)):
        head = 0
        tail = i - 1
        while head <= tail:
            if arr[i] == arr[head] + arr[tail]:
                count += 1
            if arr[i] > arr[head] + arr[tail]:
                head += 1
            else:
                tail -= 1
    return count

if __name__ == "__main__":
    arr = sys.stdin.readline().split()
    arr = [int(i) for i in arr]
    sys.stdout.write(str(triples(arr)))