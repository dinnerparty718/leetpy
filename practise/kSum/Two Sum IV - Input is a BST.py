# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build

# treverse inOrder

# time O(n) traversal inOrder dfs
# space O(n) extra space to hold the array


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        nums = []

        def inOrder(node: TreeNode):
            if not node:
                return

            inOrder(node.left)
            nums.append(node.val)
            inOrder(node.right)

        inOrder(root)

        l, r = 0, len(nums)-1

        while l < r:
            cur_sum = nums[l] + nums[r]

            if cur_sum > k:
                r -= 1
            elif cur_sum < k:
                l += 1
            else:
                return True

        return False


root = build('5,3,6,2,4,,7')
k = 28
so = Solution()

res = so.findTarget(root, k)

print(res)
