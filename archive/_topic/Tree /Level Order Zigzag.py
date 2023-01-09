# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from tree.TreeNode import TreeNode


from collections import deque
# odd level right-> left
# even level left -> right


# modify BFS

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = 0
        res = []
        queue = deque([root])

        while queue:
            n = len(queue)

            curr = [] if level % 2 == 0 else deque([])

            for _ in range(n):
                node = queue.popleft()

                if level % 2 == 0:
                    curr.append(node.val)
                else:
                    curr.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
            res.append(list(curr))
        return res


# DFS with level and reverse the list
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(node: TreeNode, level: int):
            if not node:
                return

            if level == len(res):
                res.append([])

            res[level].append(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)

        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()

        return res
