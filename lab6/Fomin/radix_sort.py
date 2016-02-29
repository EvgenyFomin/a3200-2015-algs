__author__ = 'wolfram'
import sys

def sort(arr):
    max = 0
    if __name__ != "__main__":
        arr = [str(i) for i in arr]
    for i in arr:
        if len(i) > max:
            max = len(i)
    for i in range(0, len(arr)):
        if len(arr[i]) < max:
            arr[i] = ('0' * (max - len(arr[i]))) + arr[i]
    lenlist = len(arr)
    for j in range(0, max):
        L0 = []
        L1 = []
        L2 = []
        L3 = []
        L4 = []
        L5 = []
        L6 = []
        L7 = []
        L8 = []
        L9 = []
        for i in range(0, lenlist):
            if arr[i][len(arr[i]) - j - 1] == '0':
                L0.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '1':
                L1.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '2':
                L2.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '3':
                L3.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '4':
                L4.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '5':
                L5.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '6':
                L6.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '7':
                L7.append(arr[i])
            elif arr[i][len(arr[i]) - j - 1] == '8':
                L8.append(arr[i])
            else:
                L9.append(arr[i])
        arr = L0 + L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
    for i in range(0, lenlist):
        while(arr[i][0] == '0') & (len(arr[i]) > 1):
            arr[i] = arr[i][1:len(arr[i])]
    if __name__ != "__main__":
        arr = [int(i) for i in arr]
    return arr

if __name__ == "__main__":
    a = sys.stdin.readline().split()
    a = sort(a)
    a = [str(i) for i in a]
    sys.stdout.write(' '.join(a))
