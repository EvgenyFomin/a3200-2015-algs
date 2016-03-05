__author__ = 'wolfram'

from sys import stdin

def distance(a, b):
    lines = list([len(a) * [float('inf')],
                  len(a) * [float('inf')]])
    for i in range(len(b)):
        for j in range(len(a)):
            if i == j == 0:
                if a[0] == b[0]:
                    lines[0][0] = 0
                else:
                    lines[0][0] = 1
                    # lines[0][0] = (lambda x, y: 0 if x == y else 1)(a[0], b[0])
            else:
                current, previous = lines[i % 2], lines[1 - i % 2]
                value = min(current[j - 1] + 1,
                            previous[j] + 1,
                            previous[j - 1] + int(not (a[j] == b[i])),
                            previous[j - 1] + int(not ((a[j] == b[i - 1]) and
                                                       (b[i] == a[j - 1]))))
                lines[i % 2][j] = value
    if len(a) == len(b) == 1:
        return 1
    else:
        return lines[1][len(a) - 1]


if __name__ == "__main__":
    a = stdin.readline().rstrip('\n')
    b = stdin.readline().rstrip('\n')
    print(distance(a, b))