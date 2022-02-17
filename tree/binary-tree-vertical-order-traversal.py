# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build
from collections import deque
from collections import defaultdict
# draw tree and find patterns
# BFS, level is naturally preserve


# record min and max column index to avoid sorting

'''
travese the tree using index offset, and them to defaultdict(list)  key is offset key

node offset
node.left offset -1
node.right offset + 1



record global min, global max

loop through range(min, max+1) 


'''


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


class Solution2:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # bfs

        q = deque([(root, 0)])  # node, col_index
        h = defaultdict(list)

        min_col = float('inf')
        max_col = float('-inf')

        while q:
            node, col_indx = q.popleft()

            if node:
                min_col = min(min_col, col_indx)
                max_col = max(max_col, col_indx)

                h[col_indx].append(node.val)
                q.append((node.left, col_indx - 1))
                q.append((node.right, col_indx + 1))

        if min_col == float('inf'):
            return []

        res = []

        for key in range(min_col, max_col+1):
            res.append(h[key])

        return res


so = Solution2()


root = build('3,9,20,,,15,7')


res = so.verticalOrder(root)

print(res)
