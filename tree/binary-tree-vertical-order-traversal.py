# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build
from collections import deque
from collections import defaultdict
# draw tree and find patterns
# BFS, level is naturally preserve


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # bfs

        q = deque([(root, 0)])  # node, col_index

        h = defaultdict(list)

        while q:
            node, col_indx = q.popleft()
            if node:
                h[col_indx].append(node.val)
                q.append((node.left, col_indx - 1))
                q.append((node.right, col_indx+1))

        res = []

        for key in sorted(h.keys()):
            res.append(h[key])

        return res


so = Solution()


root = build('3,9,20,,,15,7')


res = so.verticalOrder(root)

print(res)
