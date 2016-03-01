__author__ = 'wolfram'

from sys import stdin, stdout

def answer(n, palochki):
    para_1 = 0
    para_2 = 0
    palochki = sorted(palochki)

    for i in range(0, n - 2):
        if para_1 == 0:
            if palochki[n - i - 1] == palochki[n - i - 2]:
                para_1 = palochki[n - i - 1]
            elif (palochki[n - i - 1]) - 1 == palochki[n - i - 2]:
                para_1 = palochki[n - i - 2]
            else:
                palochki.pop(n - i - 1)
                continue
        if n - i - 4 < 0:
            break
        if palochki[n - i - 3] == palochki[n - i - 4]:
            para_2 = palochki[n - i - 3]
            break
        elif (palochki[n - i - 3]) - 1 == palochki[n - i - 4]:
            para_2 = palochki[n - i - 4]
            break
        else:
            palochki.pop(n - i - 3)
            continue
    return para_1 * para_2

if __name__ == "__main__":
    n = int(stdin.readline())
    palochki = stdin.readline().split()
    palochki = [int(i) for i in palochki]
    stdout.write(str(answer(n, palochki)))




