# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build


# inOrder traversal and make sure it's decending order

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur = []

        def inOrder(node: TreeNode):
            nonlocal cur
            if not node:
                return True

            result = True

            result = result and inOrder(node.left)

            if cur and cur[-1] >= node.val:
                return False
            cur.append(node.val)
            result = result and inOrder(node.right)
            return result

        return inOrder(root)


#root = build('5,4,6,3,7')
#root = build('2,1,3')
#root = build('5,1,4,,,3,6')
#root = build('3,1,5,0,2,4,6')
root = build('0,,-1')
so = Solution()

print(so.isValidBST(root))
