"""
269. Alien Dictionary
Difficulty: Hard
Topic: Dynamic Programming II

Problem Description:
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation: The order is: 'w' < 'e' < 'r' < 't' < 'f'.
"wrt" is lexicographically smaller than "wrf" because at the first position where they differ, 't' comes before 'f' in the alien language.
"er" is lexicographically smaller than "ett" because at the first position where they differ, 'r' comes before 't' in the alien language.
"ett" is lexicographically smaller than "rftt" because at the first position where they differ, 'e' comes before 'r' in the alien language.

Example 2:
Input: words = ["z","x"]
Output: "zx"
Explanation: The order is 'z' < 'x'.

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.
"""

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # TODO: Implement solution
        pass
