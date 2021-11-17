# Definition for a binary tree node.
from typing import List, Optional
from utils.buildTree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def subTreeSt(node: TreeNode) -> str:
            return ''


so = Solution()

print(build('a'))
