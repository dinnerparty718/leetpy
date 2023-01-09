# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# left == right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(n1: TreeNode, n2: TreeNode):
            if not n1 and not n2:
                return True

            if n1 and not n2 or n2 and not n1:
                return False

            return n1.val == n2.val and helper(n1.left, n2.right) and helper(n1.right, n2.left)

        return helper(root, root)
