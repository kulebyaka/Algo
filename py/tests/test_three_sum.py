import pytest
from py._15_three_sum import Solution2

class TestThreeSum:
    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
            ([], []),
            ([1, 2, 3], []),
        ],
    )
    def test_three_sum(self, nums, expected):
        solution = Solution2()
        result = solution.threeSum(nums)
        
        # Sort each triplet and the result list for comparison
        result_sorted = [sorted(triplet) for triplet in result]
        expected_sorted = [sorted(triplet) for triplet in expected]
        
        # Convert to tuples for set comparison
        result_set = {tuple(triplet) for triplet in result_sorted}
        expected_set = {tuple(triplet) for triplet in expected_sorted}
        
        assert result_set == expected_set
