# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional
from Tree.TreeNode import TreeNode

# BFS , last item in each level


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            size = len(q)
            for i in range(size):
                n = q.popleft()
                if i == size - 1:
                    res.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return res

# modified BFS
# Turing planet


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            size = len(q)
            res.append(q[0])
            for i in range(size):
                n = q.popleft()
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)

        return res
