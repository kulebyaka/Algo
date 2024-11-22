"""
33. Search in Rotated Sorted Array
Medium
Topics
Companies

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr_len = len(nums)
        right_i = arr_len-1
        left_i = 0
        while left_i < right_i:

            mid = (left_i + right_i) // 2
            if nums[mid] == target:
                return mid
            if nums[left_i] < nums[mid]: # left is sorted
                if nums[left_i] < target < nums[mid]: # target in the left
                    right_i = mid
                    continue
                else:
                    left_i = mid
                    continue

            else:  # right is sorted
                if nums[mid] < target < nums[right_i]:  # target in the right
                    left_i = mid
                    continue
                else:
                    right_i = mid
                    continue

        return -1

def main():
    # print(Solution().search([4,5,6,7,0,1,2], 0))
    print(Solution().search([4,5,6,7,0,1,2], 3))

if __name__ == "__main__":
    main()



