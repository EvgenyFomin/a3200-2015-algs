__author__ = 'wolfram'

import IlyaGame, unittest

class TestIlyaGame(unittest.TestCase):
    def test_simple_1(self):
        arr = [1, 1, 2, 2]
        result = IlyaGame.answer(len(arr), arr)
        expected = 2
        self.assertEqual(expected, result)

    def test_simple_2(self):
        arr = []
        result = IlyaGame.answer(len(arr), arr)
        expected = 0
        self.assertEqual(expected, result)

    def test_simple_3(self):
        arr = [3, 2, 1, 2]
        result = IlyaGame.answer(len(arr), arr)
        expected = 2
        self.assertEqual(expected, result)