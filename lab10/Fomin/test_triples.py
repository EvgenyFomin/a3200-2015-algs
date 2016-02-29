__author__ = 'wolfram'

import pythagorean_triples, unittest, random

class TestTriples(unittest.TestCase):
    def check_by_trivial_variant(self, arr):
        count = 0
        arr = sorted(arr)
        new_arr = []
        key = arr[0]
        new_arr.append(key)
        for i in range(1, len(arr)):
            if arr[i] != key:
                key = arr[i]
                new_arr.append(key)
        arr = new_arr
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if (pow(arr[i], 2) == pow(arr[j], 2) + pow(arr[k], 2)) & (arr[i] != arr[j]) & (arr[i] != arr[k]):
                        count += 1
        return count

    def test_simple_example_1(self):
        arr = [3, 4, 5]
        result = pythagorean_triples.triples(arr)
        expected = 1
        self.assertEqual(expected, result)

    def test_simple_example_2(self):
        arr = [10, 6, 8]
        result = pythagorean_triples.triples(arr)
        expected = 1
        self.assertEqual(expected, result)

    def test_simple_example_3(self):
        arr = [1, 2, 3]
        result = pythagorean_triples.triples(arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_simple_example_0(self):
        arr = []
        result = pythagorean_triples.triples(arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_on_random_array(self):
        arr = [random.randint(0, 100) for i in range(100)]
        print(arr)
        result = self.check_by_trivial_variant(arr)
        expected = pythagorean_triples.triples(arr)
        self.assertEqual(expected, result)