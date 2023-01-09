# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs

# Time O(n)
# Space O(n)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dia = 0

        def helper(node: TreeNode):
            nonlocal dia
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            dia = max(dia, left + right)

            return max(left, right) + 1

        helper(root)
        return dia
