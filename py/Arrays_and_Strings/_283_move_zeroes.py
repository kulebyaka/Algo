"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 1
        while j <= len(nums) - 1:
            nums_i_ = nums[i]
            nums_j_ = nums[j]
            if nums_i_ !=0 and nums_j_ != 0:
                i = i + 1
                j = j + 1
                continue

            if nums_i_ == 0 and nums_j_ != 0:
                nums[i] = nums_j_
                nums[j] = 0
                i = i + 1
                j = j + 1
                continue

            if nums_i_ == 0 and nums_j_ == 0:
                j = j + 1
                continue

            i = i + 1

class Solution1:
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


def main():
    x = [1,0,1]
    Solution().moveZeroes(x)
    print(x)
    x = [0,1,0,3,12]
    Solution().moveZeroes(x)
    print(x)
    x = [2,1]
    Solution().moveZeroes(x)
    print(x)

if __name__ == "__main__":
    main()


