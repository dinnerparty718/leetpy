# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return root


so = Solution()

root = so.deleteNode(build('5,3,6,2,4,,7'), 3)


def inorder(n: TreeNode, res: List[int]):
    if not n:
        return

    inorder(n.left, res)
    res.append(n.val)
    inorder(n.right, res)


res = []

inorder(root, res)


print(res)
