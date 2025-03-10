import pytest
from src._3_longest_substr_no_repeating_characters import Solution2

class TestLongestSubstring:
    @pytest.mark.parametrize(
        "s,expected",
        [
            ("abcabcbb", 3),   # "abc"
            ("bbbbb", 1),      # "b"
            ("pwwkew", 3),     # "wke"
            ("", 0),           # ""
            ("abcdefghijklmnopqrstuvwxyz", 26),  # Entire alphabet
            ("aab", 2),        # "ab"
            ("dvdf", 3),       # "vdf"
        ],
    )
    def test_length_of_longest_substring(self, s, expected):
        solution = Solution2()
        assert solution.lengthOfLongestSubstring(s) == expected
