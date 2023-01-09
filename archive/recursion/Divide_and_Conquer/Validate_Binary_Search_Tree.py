# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.TreeNode import TreeNode
from utils.buildTree import build


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node: Optional[TreeNode], lowerBound: int, uperBound: int):
            if not node:
                return True

            l_result = valid(node.left, lowerBound, node.val)
            r_result = valid(node.right, node.val, uperBound)

            return l_result and r_result and lowerBound < node.val < uperBound

        return valid(root, float('-inf'), float('inf'))


so = Solution()


root = build('5,4,6,,,3,7')
res = so.isValidBST(root)


print(res)
