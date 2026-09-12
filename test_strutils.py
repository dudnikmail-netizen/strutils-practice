import unittest

from strutils import is_palindrome, reverse_words, title_case


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_case_insensitive(self):
        self.assertTrue(is_palindrome("Racecar"))


class TestReverseWords(unittest.TestCase):
    def test_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")


class TestTitleCase(unittest.TestCase):
    def test_multiple_words(self):
        self.assertEqual(title_case("hello world"), "Hello World")

    def test_already_capitalized(self):
        self.assertEqual(title_case("Hello World"), "Hello World")


if __name__ == "__main__":
    unittest.main()
