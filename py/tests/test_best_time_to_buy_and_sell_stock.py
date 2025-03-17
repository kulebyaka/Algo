import pytest
from py._121_best_time_to_buy_and_sell_stock import Solution, Solution2

class TestBestTimeToBuyAndSellStock:
    @pytest.mark.parametrize(
        "prices,expected",
        [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([2, 4, 1, 7], 6),
            ([], 0),
            ([1], 0),
            ([1, 2], 1),
            ([3, 2, 6, 5, 0, 3], 4),
        ],
    )
    def test_max_profit(self, prices, expected):
        # Test the linear time solution
        solution = Solution()
        assert solution.maxProfit(prices) == expected
        
        # Test the brute force solution
        solution2 = Solution2()
        assert solution2.maxProfit(prices) == expected
