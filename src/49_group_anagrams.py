"""
49. Group Anagrams

Given an array of strings strs, group the
anagrams
together.
You can return the answer in any order.
"""
from collections import defaultdict
from typing import List


def convertIntoByteArray(str):
    # to char array
    char_array = list(str)
    char_sum=ord('0')
    for cur_char in char_array:
        char_sum^= ord(cur_char)
    return char_sum

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sum_tuple = map(lambda x: (x, convertIntoByteArray(x)), strs)
        byte_sums = list(sorted(sum_tuple, key=lambda x: x[1]))
        cur_sum=0
        cur_array = []
        for byte_sum in byte_sums:
            if cur_sum == byte_sum[1] or len(cur_array)==0:
                cur_array.append(byte_sum[0])
            else:
                res.append(cur_array)
                cur_array = [byte_sum[0]]
            cur_sum = byte_sum[1]
        res.append(cur_array)
        return res


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Create a frequency count of characters (26 slots for 'a' to 'z')
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            # Use the tuple version of the count as the key
            key = tuple(char_count)
            anagrams[key].append(word)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())


def main():
    print(Solution1().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()

