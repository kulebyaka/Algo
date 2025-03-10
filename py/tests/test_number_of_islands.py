import pytest
import copy
from py._200_islands_number import Solution

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
            ([], 0),
        ],
    )
    def test_num_islands(self, grid, expected):
        # We need to create a deep copy of the grid for each test
        # because the solution modifies the grid
        grid_copy = copy.deepcopy(grid)
        solution = Solution()
        assert solution.numIslands(grid_copy) == expected

    def test_empty_grid(self):
        solution = Solution()
        assert solution.numIslands([]) == 0
        
    def test_single_island(self):
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        solution = Solution()
        assert solution.numIslands(grid) == 1
        
    def test_no_islands(self):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        solution = Solution()
        assert solution.numIslands(grid) == 0
        
    def test_diagonal_islands(self):
        # Diagonal cells are not connected
        grid = [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"]
        ]
        solution = Solution()
        assert solution.numIslands(grid) == 5
