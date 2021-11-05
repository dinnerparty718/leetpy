# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.TreeNode import TreeNode

# time O(n)
# space depends if the tree is balanced or not
# best case O(logn)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if node is None:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            # max()
            return max(left, right) + 1

        return helper(root)


solution = Solution()


root = TreeNode(1)

left, right = TreeNode(2), TreeNode(3)

root.left = left
root.right = right
root.right.left, root.right.right = TreeNode(4), TreeNode(5)

root.right.left.left, root.right.left.right = TreeNode(6), TreeNode(7)

root.right.left.left.left = TreeNode(8)

root.right.left.left.left.left = TreeNode(10)

root.right.left.right.right = TreeNode(9)


result = solution.maxDepth(root)


print(result)
