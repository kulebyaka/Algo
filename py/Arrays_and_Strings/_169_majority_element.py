"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n // 2
        hashset = dict()

        for num in nums:
            cur = hashset.get(num)
            if cur is None:
                cur = 0

            hashset[num] = cur + 1

            if cur >= majority:
                return num

        return 0

def main():
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([1]))

if __name__ == "__main__":
    main()