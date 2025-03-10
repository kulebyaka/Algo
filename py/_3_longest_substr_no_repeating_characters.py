"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring
without repeating characters.
"""

class Solution1:
    def areCharactersUnique(self, s:str):

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

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # HashSet to store unique characters
        unique_chars = set()
        max_length = 0
        left = 0  # Left pointer of the sliding window

        # Move right pointer to expand the window
        for right in range(len(s)):
            # If character is already in the set, shrink the window from the left
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            # Add the current character to the set
            unique_chars.add(s[right])
            # Update max_length
            max_length = max(max_length, right - left + 1)

        return max_length

def main():
    print(Solution1().lengthOfLongestSubstring("abcadkcbb"))
    print(Solution2().lengthOfLongestSubstring("abcadkcbb"))

if __name__ == "__main__":
    main()
