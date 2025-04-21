"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Constraints:

    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)
            elif char in '}])':
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                match top_element:
                    case '(':
                        if char == ')':
                            continue
                        return False
                    case '[':
                        if char == ']':
                            continue
                        return False
                    case '{':
                        if char == '}':
                            continue
                        return False
                if char != top_element:
                    return False
            else:
                return False
        return len(stack)==0

def main():
    print(Solution().isValid("([])[]["))

if __name__ == "__main__":
    main()
