# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build


# important declar self.res or nonlocal res

# time O(n)
# space O(n) implict stack. if balanced O(logn)


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = float('-inf')

        # bottom up
        def helper(node: TreeNode) -> int:

            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            # print(node.val, left, right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1

        helper(root)

        return self.res


so = Solution()

root = build('1,2')


result = so.diameterOfBinaryTree(root)

print(result)
