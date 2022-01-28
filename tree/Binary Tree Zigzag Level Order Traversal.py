# Definition for a binary tree node.

from typing import List, Optional
from collections import deque
from utils.buildTree import build
from tree.TreeNode import TreeNode

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# normal BFS reverse the list when encounter odd level
# Time O(N)
# space O(N)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        level = 0

        res = []

        while q:
            size = len(q)
            cur = []
            for _ in range(size):
                node = q.popleft()
                cur.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 1:
                res.append(cur[::-1])
            else:
                res.append(cur)

            level += 1

        return res


# DFS
# pre-order iterative
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()

            if level == len(res):
                res.append(deque([node.val]))
            else:
                if level % 2 == 1:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)
            # stack, first in last out
            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        return res


# DFS recursive
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node: TreeNode, level: int, res: List[List[int]]):
            if not node:
                return

            if level == len(res):
                res.append(deque([node.val]))
            else:
                if level % 2 == 1:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)

            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)

        dfs(root, 0, res)

        return res


so = Solution()

root = build('3,9,20,,,15,7')


res = so.zigzagLevelOrder(root)

print(res)
