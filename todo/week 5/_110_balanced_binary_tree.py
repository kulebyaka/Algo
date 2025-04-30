"""
110. Balanced Binary Tree
Difficulty: Easy
Topic: Trees & BSTs

Problem Description:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Explanation: The left subtree of root node (with value 9) has depth 1, and the right subtree of root (with value 20) has depth 2. The difference is 1, which is allowed.

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Explanation: The left subtree of the subtree rooted at 2 has depth 3, and the right subtree has depth 1. The difference is 2, which is not allowed.

Example 3:
Input: root = []
Output: true
Explanation: An empty tree is considered height-balanced.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # TODO: Implement solution
        pass
