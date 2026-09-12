import unittest

from strutils import is_palindrome, reverse_words, title_case


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))


class TestReverseWords(unittest.TestCase):
    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")


if __name__ == "__main__":
    unittest.main()
