__author__ = 'wolfram'

import palindrome, unittest

class Test(unittest.TestCase):
    def test_simple_1(self):
        s = "abca"
        self.assertEqual(palindrome.palindrome(s), "aba")

    def test_simple_2(self):
        s = "babcad"
        self.assertEqual(palindrome.palindrome(s), "bab")

    def test_empty(self):
        s = ""
        self.assertEqual(palindrome.palindrome(s), "")

    def test_simple_3(self):
        s = "a"
        self.assertEqual(palindrome.palindrome(s), "a")

    def test_simple_4(self):
        s = "ab"
        self.assertEqual(palindrome.palindrome(s), "a")

    def test_hard_1(self):
        s = "abacabadabacaba"
        self.assertEqual(palindrome(s), "abacabadabacaba")

    def test_hard_2(self):
        s = "abacabazzzzzzz"
        self.assertEqual(palindrome(s), "abacaba")

    def test_hard_3(self):
        s = "ghgaxybtltcmdinnefuvjegkodpcwozbzqqarjj"
        self.assertEqual(palindrome.palindrome(s), "abcdefedcba")
