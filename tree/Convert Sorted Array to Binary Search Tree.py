# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from Tree.TreeNode import TreeNode
from Tree.traversal.dfs_recursion import inOrder


# own pick the middle value as a root, but use nums slice
# refer leetcode solution using left, right pointer
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # pick the middle number

        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        l = 0
        r = len(nums)-1

        mid_index = l + (r-l)//2

        root = TreeNode(nums[mid_index])

        root.left = self.sortedArrayToBST(nums[0:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index+1:])
        return root


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int):
            if left > right:
                return None

            # always choose left middle node as a root
            p = left + (right-left)//2

            # pre-order traversal node-> left -> right

            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)

            return root

        return helper(0, len(nums)-1)


so = Solution()

nums = [-10, -3, 0, 5, 9]

so = Solution()

root = so.sortedArrayToBST(nums)


inOrder(root)
