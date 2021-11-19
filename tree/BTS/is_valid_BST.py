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
# time O(n)
# space O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inOrder(node: TreeNode):
            nonlocal prev
            if not node:
                return True

            if inOrder(node.left) == False:
                return False

            if prev != None and prev >= node.val:
                return False
            prev = node.val
            return inOrder(node.right)

        return inOrder(root)


# solution2 upperlimit and lowerlimit
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node: TreeNode, lower_bound: int, upper_bound: int):
            if not node:
                return True
            return lower_bound < node.val < upper_bound and isValid(node.left, lower_bound, node.val) and isValid(node.right, node.val, upper_bound)

        return isValid(root, float('-inf'), float('inf'))


root = build('5,4,6,3,7')
#root = build('2,1,3')
#root = build('5,1,4,,,3,6')
#root = build('3,1,5,0,2,4,6')
#root = build('0,,-1')
so = Solution()

print(so.isValidBST(root))
