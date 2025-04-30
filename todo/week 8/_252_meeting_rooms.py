"""
252. Meeting Rooms
Difficulty: Easy
Topic: Greedy & Intervals

Problem Description:
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: The person cannot attend all meetings because the meetings [0,30] and [5,10] overlap.

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: The person can attend all meetings because they do not overlap.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6
"""

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # TODO: Implement solution
        pass
