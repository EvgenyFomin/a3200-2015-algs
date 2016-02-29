__author__ = 'wolfram'

import radix_sort
import unittest
import random

class TestRadixSort(unittest.TestCase):
    def check_sort(self, arr):
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                return False
        return True

    def test_empty(self):
        arr = []
        result = radix_sort.sort(arr)
        expected = []
        self.assertEqual(expected, result)

    def test_with_equal_elements(self):
        arr = [3, 3, 2, 2, 1, 1, 1, 0]
        result = radix_sort.sort(arr)
        expected = [0, 1, 1, 1, 2, 2, 3, 3]
        self.assertEqual(expected, result)

    def test_with_one_random_element(self):
        one_element = random.randint(0, 100000)
        arr = [one_element]
        result = radix_sort.sort(arr)
        expected = [one_element]
        self.assertEqual(expected, result)

    def test_with_random_elements(self):
        arr = [random.randint(0, 100000) for i in range(50)]
        result = radix_sort.sort(arr)
        self.assertTrue(self.check_sort(result))