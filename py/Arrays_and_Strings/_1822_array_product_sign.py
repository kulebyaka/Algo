"""
1822. Sign of the Product of an Array

Implement a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for i in nums:
            if i<0:
                s = -s
            elif i==0:
                return 0

        return s


