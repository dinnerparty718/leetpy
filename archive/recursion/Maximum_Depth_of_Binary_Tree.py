# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(n) visit each node exactly once
# Space O(n) worst case, O(logN) best case when the tree is balanced


from typing import Optional
from Tree.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


# iterative using stack with DFS
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = float('-inf')

        if not root:
            return 0

        s = [(1, root)]

        while s:
            depth, node = s.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                s.append((depth+1, node.left))

            if node.right:
                s.append((depth+1, node.right))

        return max_depth
