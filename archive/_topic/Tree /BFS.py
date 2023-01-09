# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from typing import List, Optional
from tree.TreeNode import TreeNode


# queue
# Time O(n)
# space O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = collections.deque([root])

        while queue:
            n = len(queue)
            curr = []

            for _ in range(n):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(curr)

        return res


# recursion
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1)

            if node.right:
                helper(node.right, level+1)

        helper(root, 0)

        return levels
