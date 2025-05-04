"""
128. Longest Consecutive Sequence
Difficulty: Medium
Topic: Arrays & Hashing

Problem Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = dict()
        max_seq = 0

        for num in nums:
            cur = hashset.get(num - 1)
            if cur is None:
                cur = 0
            hashset[num] = cur + 1
            max_seq = max(max_seq, cur + 1)
            if cur > 0:
                hashset.pop(num)

        return max_seq

def main():
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

if __name__ == "__main__":
    main()


