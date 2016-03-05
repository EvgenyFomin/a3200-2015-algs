__author__ = 'wolfram'

import levenshtein, unittest

class TestLevenshtein(unittest.TestCase):
    def test1(self):
        a = 'Levenshtien'
        b = 'Frankenstein'
        res = levenshtein.distance(a, b)
        exp = 7
        self.assertEqual(res, exp)

    def test2(self):
        a = 'Petooshock'
        b = 'Toornickman'
        res = levenshtein.distance(a, b)
        exp = 8
        self.assertEqual(res, exp)

    def test3(self):
        a = 'Assassin'
        b = 'Killer'
        res = levenshtein.distance(a, b)
        exp = 8
        self.assertEqual(res, exp)
