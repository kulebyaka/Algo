import pytest
from py._33_search_in_rotated_sorted_array import Solution

class TestRotatedSearch:
    @pytest.mark.parametrize(
        "nums,target,expected",
        [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
            ([], 5, -1),
            ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
            ([1, 3], 3, 1),
            ([3, 1], 3, 0),
            ([5, 1, 3], 5, 0),
        ],
    )
    def test_search(self, nums, target, expected):
        solution = Solution()
        assert solution.search(nums, target) == expected
        
    def test_no_rotation(self):
        # Test when array is not rotated
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        assert solution.search(nums, 3) == 2
        
    def test_full_rotation(self):
        # Test when array is rotated completely (back to original)
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        assert solution.search(nums, 1) == 0
