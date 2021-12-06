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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []

        # top down
        def dfs(node: TreeNode, cur: List[str], res: List[str]) -> List[int]:
            if not node.left and not node.right:
                cur.append(str(node.val))
                res.append('->'.join(cur))
                return

            cur.append(str(node.val))

            if node.left:
                dfs(node.left, cur[:], res)
            if node.right:
                dfs(node.right, cur[:], res)

        dfs(root, [], res)
        return res


so = Solution()

root = build('1')

res = so.binaryTreePaths(root)


print(res)
