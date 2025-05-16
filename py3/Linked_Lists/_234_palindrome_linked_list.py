"""
234. Palindrome Linked List
Difficulty: Easy
Topic: Linked Lists

Problem Description:
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # stack-based approach
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        stack_pointer = head
        fast_pointer = head
        stack = []
        collected = False
        while stack_pointer:
            if not collected:
                stack.append(stack_pointer.val)
            else:
                cur = stack.pop()
                if cur != stack_pointer.val:
                    return False
            stack_pointer = stack_pointer.next
            if collected:
                continue
            fast_pointer = fast_pointer.next
            if not fast_pointer:
                stack.pop()
                collected = True
                continue
            fast_pointer = fast_pointer.next
            if not fast_pointer:
                collected = True
                continue

        return True

    # linked list half-reorder approach
    def isPalindrome2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        # Reverse the first half while finding the middle
        prev = None
        while fast and fast.next:
            fast = fast.next.next

            # Reverse the current node
            next_temp = slow.next
            slow.next = prev
            prev = slow
            slow = next_temp

        # If the list has odd number of elements, skip the middle one
        if fast:
            slow = slow.next

        # Compare the reversed first half (prev) with the second half (slow)
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True


    def createLinkedList(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


def test_palindrome_linked_list():
    solution = Solution()
    #
    # Test case 1: Regular palindrome [1,2,2,1]
    assert solution.isPalindrome(solution.createLinkedList([1, 2, 2, 1])) == True
    assert solution.isPalindrome2(solution.createLinkedList([1, 2, 2, 1])) == True

    # Test case 5: Odd length palindrome [1,2,3,2,1]
    assert solution.isPalindrome(solution.createLinkedList([1, 2, 3, 2, 1])) == True
    assert solution.isPalindrome2(solution.createLinkedList([1, 2, 3, 2, 1])) == True

    # Test case 2: Non-palindrome [1,2]
    assert solution.isPalindrome(solution.createLinkedList([1, 2])) == False
    assert solution.isPalindrome2(solution.createLinkedList([1, 2])) == False

    # Test case 6: Non-palindrome [1,2,3,4]
    assert solution.isPalindrome(solution.createLinkedList([1, 2, 3, 4])) == False
    assert solution.isPalindrome2(solution.createLinkedList([1, 2, 3, 4])) == False

    # Test case 3: Single element [1]
    assert solution.isPalindrome(solution.createLinkedList([1])) == True
    assert solution.isPalindrome2(solution.createLinkedList([1])) == True

    # Test case 4: Empty list
    assert solution.isPalindrome(None) == True
    assert solution.isPalindrome2(None) == True


if __name__ == "__main__":
    test_palindrome_linked_list()
    print("All test cases passed!")




