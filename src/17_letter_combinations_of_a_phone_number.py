"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


"""
from typing import List


class Solution:
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def rec(self, digits: str, pos: int, arrays: List[str]):
        if pos >= len(digits):
            return arrays

        new_arrays = []
        for res in arrays:
            for i, ch in enumerate(self.keyboard[digits[pos]]):
                new_arrays.append(res + ch)
        return self.rec(digits, pos+1, new_arrays)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = [""]
        return self.rec(digits, 0, res)


def main():
    print(Solution().letterCombinations("23"))

if __name__ == "__main__":
    main()

