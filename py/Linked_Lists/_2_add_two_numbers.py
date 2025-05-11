"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        result = result_head
        remainder = 0
        while l1 or l2 or remainder:
            cur1 = l1.val if l1 else 0
            cur2 = l2.val if l2 else 0
            cur_sum = cur1 + cur2 + remainder
            remainder = cur_sum // 10
            digit = cur_sum % 10
            result.val = digit

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if  l1 or l2 or remainder:
                result.next = ListNode()
                result = result.next

        return result_head

def main():
    l1 = ListNode(2, ListNode(4 , ListNode(3)))
    l2 = ListNode(5, ListNode(6 , ListNode(4)))
    res = Solution().addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next

if __name__ == "__main__":
    main()






