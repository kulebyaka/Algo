"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring
without repeating characters.
"""

class Solution:
    def areCharactersUnique(self, s:str):

        # An integer to store presence/absence
        # of 26 characters using its 32 bits
        checker = 0

        print("check " + s)
        for i in range(len(s)):

            val = ord(s[i]) - ord('a')

            # If bit corresponding to current
            # character is already set
            if (checker & (1 << val)) > 0:
                return False

            # set bit in checker
            checker |= (1 << val)

        print(s + " is unique")
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_res = 0
        for i in range(len(s)):
            for k in range(1, len(s)):
                if k>max_res and (k+i)<=len(s) and self.areCharactersUnique(s[i:k+i]):
                    max_res = k

        return max_res

def main():
    print(Solution().lengthOfLongestSubstring("abcabcbb"))

if __name__ == "__main__":
    main()