import pytest
import os
import sys
from typing import List, Callable, Any, Dict, Tuple

# Add the src directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import solutions
from src._146_LRU_cache import LRUCache
from src._151_reverse_words_in_a_string import Solution as ReverseWordsSolution
from src._15_three_sum import Solution2 as ThreeSumSolution
from src._17_letter_combinations_of_a_phone_number import Solution as LetterCombinationsSolution
from src._1822_array_product_sign import Solution as ArraySignSolution
from src._200_islands_number import Solution as IslandsSolution
from src._33_search_in_rotated_sorted_array import Solution as RotatedSearchSolution
from src._3_longest_substr_no_repeating_characters import Solution2 as LongestSubstringSolution
from src._49_group_anagrams import Solution1 as GroupAnagramsSolution
from src._54_spiral_matrix import Solution54 as SpiralMatrixSolution


# Tests for LRU Cache
class TestLRUCache:
    def test_basic_operations(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)
        assert cache.get(2) == -1
        cache.put(4, 4)
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_edge_cases(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        assert cache.get(1) == 1
        cache.put(2, 2)
        assert cache.get(1) == -1
        assert cache.get(2) == 2


# Tests for Reverse Words
class TestReverseWords:
    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("the sky is blue", "blue is sky the"),
            ("  hello world  ", "world hello"),
            ("a good   example", "example good a"),
            ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
            ("Alice does not even like bob", "bob like even not does Alice"),
        ],
    )
    def test_reverse_words(self, input_str, expected):
        solution = ReverseWordsSolution()
        assert solution.reverseWords(input_str) == expected


# Tests for Three Sum
class TestThreeSum:
    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ],
    )
    def test_three_sum(self, nums, expected):
        solution = ThreeSumSolution()
        result = solution.threeSum(nums)
        
        # Sort results for comparison
        result_sorted = [sorted(x) for x in result]
        expected_sorted = [sorted(x) for x in expected]
        
        # Convert to tuple for set comparison
        result_tuples = [tuple(x) for x in result_sorted]
        expected_tuples = [tuple(x) for x in expected_sorted]
        
        assert set(result_tuples) == set(expected_tuples)


# Tests for Letter Combinations
class TestLetterCombinations:
    @pytest.mark.parametrize(
        "digits,expected",
        [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("", []),
            ("2", ["a", "b", "c"]),
            ("234", ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", 
                    "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", 
                    "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]),
        ],
    )
    def test_letter_combinations(self, digits, expected):
        solution = LetterCombinationsSolution()
        result = solution.letterCombinations(digits)
        assert sorted(result) == sorted(expected)


# Tests for Array Sign
class TestArraySign:
    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([-1, -2, -3, -4, 3, 2, 1], 1),
            ([1, 5, 0, 2, -3], 0),
            ([-1, 1, -1, 1, -1], -1),
            ([-1], -1),
            ([1], 1),
            ([0], 0),
        ],
    )
    def test_array_sign(self, nums, expected):
        solution = ArraySignSolution()
        assert solution.arraySign(nums) == expected


# Tests for Number of Islands
class TestNumberOfIslands:
    @pytest.mark.parametrize(
        "grid,expected",
        [
            ([["1", "1", "1", "1", "0"], 
              ["1", "1", "0", "1", "0"], 
              ["1", "1", "0", "0", "0"], 
              ["0", "0", "0", "0", "0"]], 1),
            ([["1", "1", "0", "0", "0"], 
              ["1", "1", "0", "0", "0"], 
              ["0", "0", "1", "0", "0"], 
              ["0", "0", "0", "1", "1"]], 3),
            ([["0"]], 0),
            ([["1"]], 1),
        ],
    )
    def test_num_islands(self, grid, expected):
        # We need to create a deep copy of the grid for each test
        # because the solution modifies the grid
        import copy
        grid_copy = copy.deepcopy(grid)
        solution = IslandsSolution()
        assert solution.numIslands(grid_copy) == expected


# Tests for Rotated Search
class TestRotatedSearch:
    @pytest.mark.parametrize(
        "nums,target,expected",
        [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
        ],
    )
    def test_search(self, nums, target, expected):
        solution = RotatedSearchSolution()
        assert solution.search(nums, target) == expected


# Tests for Longest Substring
class TestLongestSubstring:
    @pytest.mark.parametrize(
        "s,expected",
        [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("au", 2),
            ("dvdf", 3),
        ],
    )
    def test_length_of_longest_substring(self, s, expected):
        solution = LongestSubstringSolution()
        assert solution.lengthOfLongestSubstring(s) == expected


# Tests for Group Anagrams
class TestGroupAnagrams:
    def test_group_anagrams(self):
        solution = GroupAnagramsSolution()
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = solution.groupAnagrams(input_strs)
        
        # We need to check that anagrams are grouped together
        # First, sort each group
        sorted_groups = []
        for group in result:
            sorted_groups.append(sorted(group))
        
        # Sort the groups by their first element for consistent comparison
        sorted_groups.sort(key=lambda x: x[0] if x else "")
        
        # Expected output (sorted for comparison)
        expected = [
            ["ate", "eat", "tea"],
            ["bat"],
            ["nat", "tan"]
        ]
        expected.sort(key=lambda x: x[0] if x else "")
        
        # Check that the groups match
        assert len(sorted_groups) == len(expected)
        
        # Check each group has the same elements
        for i, group in enumerate(sorted_groups):
            assert set(group) == set(expected[i])


# Tests for Spiral Matrix
class TestSpiralMatrix:
    @pytest.mark.parametrize(
        "matrix,expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            ([[1]], [1]),
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            ([], []),
        ],
    )
    def test_spiral_order(self, matrix, expected):
        solution = SpiralMatrixSolution()
        assert solution.spiral_order(matrix) == expected
