from typing import Optional
from typing import List

from Tree.traversal.dfs_recursion import inOrder

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        stack = [root]
        res = []

        while stack:
            n = stack.pop()

        pass


root = TreeNode(0)
left, right = TreeNode(1), TreeNode(2)

root.left = left
root.right = right

l, r = TreeNode(3), TreeNode(4)
left.left = l
left.right = r


right.left = TreeNode(5)

inOrder(root)
