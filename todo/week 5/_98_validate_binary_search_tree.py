"""
98. Validate Binary Search Tree
Difficulty: Medium
Topic: Trees & BSTs

Problem Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true
Explanation: 
The tree structure is:
    2
   / \
  1   3
This is a valid BST.

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: 
The tree structure is:
    5
   / \
  1   4
     / \
    3   6
The root node's value is 5 but its right child's value is 4, which is less than 5.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # TODO: Implement solution
        pass
