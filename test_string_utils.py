import unittest

from string_utils import (
    reverse_string,
    to_uppercase,
    is_palindrome
)

class TestStringUtils(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    def test_uppercase(self):
        self.assertEqual(to_uppercase("hello"),"HELLO")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

if __name__ == "__main__":
    unittest.main()