__author__ = 'wolfram'

import unittest, histogram

class TestHistogram(unittest.TestCase):
    def test_example(self):
        arr = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        result = histogram.squares(arr)
        expected = 10
        self.assertEqual(expected, result)

    def test_simple_0(self):
        arr = []
        result = histogram.squares(arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_simple_1(self):
        arr = [1, 2, 3]
        result = histogram.squares(arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_simple_2(self):
        arr = [3, 2, 1]
        result = histogram.squares(arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_simple_3(self):
        arr = [3, 1, 2]
        result = histogram.squares(arr)
        expected = 1
        self.assertEqual(expected, result)

    def test_simple_3(self):
        arr = [5, 5, 5, 5, 4, 6]
        result = histogram.squares(arr)
        expected = 1
        self.assertEqual(expected, result)

    def test_simple_4(self):
        arr = [5, 5, 5, 5]
        result = histogram.squares(arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_simple_5(self):
        arr = [2, 3, 4, 5, 1, 3, 7, 9, 10, 5, 6, 7, 9]
        result = histogram.squares(arr)
        expected = 9
        self.assertEqual(expected, result)

    def test_simple_6(self):
        arr = [5, 1, 3, 2, 4, 3, 2, 1, 2]
        result = histogram.squares(arr)
        expected = 6
        self.assertEqual(expected, result)

    def test_simple_7(self):
        arr = [1, 3, 2, 1, 0]
        result = histogram.squares(arr)
        expected = 0
        self.assertEqual(expected, result)