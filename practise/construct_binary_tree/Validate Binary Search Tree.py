# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from tree.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def helper(node: TreeNode, lower: int, upper: int) -> bool:
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            left_valid = helper(node.left, lower, node.val)
            right_valid = helper(node.right, node.val, upper)

            return left_valid and right_valid

        return helper(root, float('-inf'), float('inf'))
