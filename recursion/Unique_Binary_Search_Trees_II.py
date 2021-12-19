# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from Tree.TreeNode import TreeNode
from Tree.Codec import Codec


class Solution:

    def insertNode(self, node, n):
        pass

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n <= 0:
            return []

        res = [TreeNode(0)]


so = Solution()


n = 3

res = so.generateTrees(n)


cod = Codec()

for t in res:
    print(cod.serialize2(t))
