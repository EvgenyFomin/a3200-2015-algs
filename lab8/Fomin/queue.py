__author__ = 'wolfram'

import sys

class Queue:
    def pop(self):
        pass

    def push(self, item):
        pass

    def size(self):
        pass


class StacksQueue(Queue):
    def __init__(self):
        self._arr = []

    def push(self, a):
        self._arr.append(a)

    def pop(self):
        return self._arr.pop()

    def size(self):
        return len(self._arr)


class MaxElementQueue(Queue):
    def __init__(self):
        self._negative_inf = - (2 ** 128)
        self._left_stack = StacksQueue()
        self._right_stack = StacksQueue()
        self._max_stack = []
        self._max = self._negative_inf
        self._max_stack.append(self._negative_inf)
        self._size = 0

    def push(self, elem):
        self._left_stack.push(elem)
        if elem > self._max:
            self._max = elem
        self._size += 1

    def pop(self):
        if self._right_stack.size() == 0:
            length = self._left_stack.size()
            local_max = self._negative_inf
            self._max = self._negative_inf
            for i in range(length):
                elem = self._left_stack.pop()
                self._right_stack.push(elem)
                if elem > local_max:
                    local_max = elem
                self._max_stack.append(local_max)
        self._size -= 1
        self._max_stack.pop()
        return self._right_stack.pop()

    def size(self):
        return self._size

    def max(self):
        index = len(self._max_stack) - 1
        return max(self._max, self._max_stack[index])


def output(string, max_element_queue):
    string = string.split("\n")[0]
    if string == "max":
        if max_element_queue.size() > 0:
            return str(max_element_queue.max())
        return "empty"
    elif string == "pop":
        if max_element_queue.size() > 0:
            return str(max_element_queue.pop())
        return "empty"
    word, value = string.split()
    max_element_queue.push(int(value))
    return "ok"


if __name__ == "__main__":
    queue = MaxElementQueue()
    while True:
        line = sys.stdin.readline()
        print(output(line, queue))