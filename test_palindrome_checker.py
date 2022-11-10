"""
Author: Logan Maupin
Date: 11/09/2022

This is my first testing script I've ever written, and it's pretty fun! I could get used to this1
I still have so much to learn in Python, but I'm really proud of how far I've come so far. I can't wait
to continue my journey forward with this language and other programming languages.
"""


import unittest
from palindrome_checker import palindrome_test


class TestPalindrome(unittest.TestCase):

    def test_palindrome_test(self):
        self.assertEqual(True, palindrome_test("racecar"))
        self.assertEqual(True, palindrome_test("Racecar"))
        self.assertEqual(False, palindrome_test("Racecar123"))
        self.assertEqual(False, palindrome_test(""))
        self.assertEqual(False, palindrome_test("123racecar"))
