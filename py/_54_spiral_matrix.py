"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List

class Solution54:
    @staticmethod
    def spiral_order(matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left < right and top < bottom:
            result.extend([matrix[top][i] for i in range(left, right)])
            result.extend([matrix[i][right] for i in range(top, bottom)])
            result.extend([matrix[bottom][i] for i in range(right, left, -1)])
            result.extend([matrix[i][left] for i in range(bottom, top, -1)])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        if left == right:
            result.extend([matrix[i][left] for i in range(top, bottom + 1)])
        elif top == bottom:
            result.extend([matrix[top][i] for i in range(left, right + 1)])
        return result

def main():
    print(Solution54().spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

if __name__ == "__main__":
    main()