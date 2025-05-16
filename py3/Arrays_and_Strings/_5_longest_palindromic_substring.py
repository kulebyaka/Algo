"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""


# A function to print a substring.
def printSubstring(str, left, right):
    for i in range(left, right + 1):
        print(str[i])

# Manacher's algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If length of given string is n then its length after
        # inserting n+1 "#", one "@", and one "$" will be
        # (n) + (n+1) + (1) + (1) = 2n+3
        strLen = 2 * len(s) + 3
        sChars = [0] * strLen

        # Inserting special characters to ignore special cases
        # at the beginning and end of the array
        # "abc" -> @ # a # b # c # $
        # "" -> @#$
        # "a" -> @ # a # $
        sChars[0] = '@'
        sChars[strLen - 1] = '$'
        t = 1
        for i in s:
            sChars[t] = '#'
            t += 1
            sChars[t] = i
            t += 1

        sChars[t] = '#'

        maxLen = int(0)
        start = int(0)
        maxRight = int(0)
        center = int(0)
        p = [0] * strLen  # i's radius, which doesn't include i
        for i in range(1, strLen - 1):
            if i < maxRight:
                p[i] = min(maxRight - i, p[2 * center - i])

            # Expanding along the center
            while sChars[i + p[i] + 1] == sChars[i - p[i] - 1]:
                p[i] += 1

            # Updating center and its bound
            if i + p[i] > maxRight:
                center = i
                maxRight = i + p[i]

            # Updating ans
            if p[i] > maxLen:
                start = int((i - p[i] - 1) / 2)
                maxLen = p[i]

        # Printing the longest Palindromic substring
        print("The Longest Palindromic Substring is: ")
        return printSubstring(s, start, start + maxLen - 1)

