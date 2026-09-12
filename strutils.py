def is_palindrome(s):
    """Return True if s reads the same forwards and backwards (case-insensitive)."""
    normalized = s.lower()
    return normalized == normalized[::-1]


def reverse_words(s):
    """Reverse the order of whitespace-separated words in s."""
    return " ".join(reversed(s.split()))


def title_case(s):
    """Capitalize the first letter of each word in s."""
    return " ".join(word.capitalize() for word in s.split())
