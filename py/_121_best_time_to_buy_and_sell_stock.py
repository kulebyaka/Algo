"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List

from py.benchmarks.auto_discovery.benchmark_metadata import BenchmarkInfo


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute force approach.
        Time complexity: O(n²)
        Space complexity: O(1)
        """
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find maximum profit by buying and selling stock once.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not prices or len(prices) < 2:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            # Update max profit if selling at current price gives better profit
            max_profit = max(max_profit, price - min_price)
            # Update minimum price seen so far
            min_price = min(min_price, price)

        return max_profit

def main():
    sol = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],  # Expected: 5 (buy at 1, sell at 6)
        [7, 6, 4, 3, 1],     # Expected: 0 (decreasing prices, no profit)
        [2, 4, 1, 7],        # Expected: 6 (buy at 1, sell at 7)
    ]
    
    for prices in test_cases:
        print(f"Prices: {prices}, Max Profit: {sol.maxProfit(prices)}")


if __name__ == "__main__":
    main()


# Custom benchmark configuration - will be used instead of auto-inference
def generate_stock_prices(size: int) -> List[int]:
    """Generate random stock prices for benchmarking."""
    import random
    # Generate a sequence of prices with some trends to make it realistic
    base = 100
    prices = []
    for _ in range(size):
        # Random walk with some volatility
        base += random.randint(-5, 5)
        base = max(base, 1)  # Prevent negative or zero prices
        prices.append(base)
    return prices

# Define custom benchmark info
BENCHMARK_INFO = BenchmarkInfo(
    input_generator=generate_stock_prices,
    input_sizes=[10, 100, 1000, 10000, 50000],
    num_runs=3,
    name="Stock Trading Profit Optimization"
)
