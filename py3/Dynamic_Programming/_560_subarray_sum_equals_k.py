"""
560. Subarray Sum Equals K
Difficulty: Medium
Topic: Arrays & Hashing

Problem Description:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

from typing import List

# brute force, O(n^2)
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                if cur_sum == k:
                    result += 1

        return result

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1

        for num in nums:
            prefix_sum += num  # Update the running prefix sum
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
            else:
                prefix_sum_count[
                    prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time

        return count


def main():
    print(Solution1().subarraySum([1,2,3],3))

if __name__ == "__main__":
    main()
